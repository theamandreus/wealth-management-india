#!/usr/bin/env python3
"""
MCP Server for Indian Mutual Fund Data.

Wraps the free mfapi.in API to provide mutual fund search, NAV history,
return calculations, SIP simulations, and fund comparisons. Designed to
work with the India Wealth Management Plugin skills.

Data source: https://api.mfapi.in (free, no auth, daily NAV updates from AMFI)
"""

from typing import Optional, List, Dict, Any
from enum import Enum
from datetime import datetime, timedelta
from statistics import stdev, mean
import json
import math

import httpx
from pydantic import BaseModel, Field, field_validator, ConfigDict
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("india_mf_mcp")

# Constants
API_BASE_URL = "https://api.mfapi.in"
CACHE_TTL_SECONDS = 3600  # 1 hour cache for NAV data
DATE_FORMAT = "%d-%m-%Y"

# Simple in-memory cache
_nav_cache: Dict[str, Dict[str, Any]] = {}


# ─── Shared Utilities ───────────────────────────────────────────────────────

async def _make_api_request(endpoint: str) -> Any:
    """Reusable function for all mfapi.in API calls."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}/{endpoint}",
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()


def _handle_api_error(e: Exception) -> str:
    """Consistent error formatting across all tools."""
    if isinstance(e, httpx.HTTPStatusError):
        if e.response.status_code == 404:
            return "Error: Fund not found. Please check the scheme code is correct. Use india_mf_search to find valid scheme codes."
        elif e.response.status_code == 429:
            return "Error: Rate limit exceeded. Please wait a moment before making more requests."
        return f"Error: API request failed with status {e.response.status_code}"
    elif isinstance(e, httpx.TimeoutException):
        return "Error: Request timed out. The mfapi.in server may be slow. Please try again."
    return f"Error: {type(e).__name__}: {str(e)}"


async def _get_nav_history(scheme_code: int) -> Dict[str, Any]:
    """Fetch and cache NAV history for a scheme."""
    cache_key = str(scheme_code)
    now = datetime.now().timestamp()

    if cache_key in _nav_cache:
        cached = _nav_cache[cache_key]
        if now - cached["fetched_at"] < CACHE_TTL_SECONDS:
            return cached["data"]

    data = await _make_api_request(f"mf/{scheme_code}")

    if data.get("status") != "SUCCESS":
        raise ValueError(f"API returned status: {data.get('status')}")

    _nav_cache[cache_key] = {"data": data, "fetched_at": now}
    return data


def _parse_nav_data(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Parse NAV data into sorted list of {date, nav} dicts."""
    entries = []
    for entry in data.get("data", []):
        try:
            date = datetime.strptime(entry["date"], DATE_FORMAT)
            nav = float(entry["nav"])
            entries.append({"date": date, "nav": nav})
        except (ValueError, KeyError):
            continue
    entries.sort(key=lambda x: x["date"])
    return entries


def _calculate_cagr(start_nav: float, end_nav: float, years: float) -> float:
    """Calculate CAGR given start NAV, end NAV, and period in years."""
    if start_nav <= 0 or years <= 0:
        return 0.0
    return ((end_nav / start_nav) ** (1 / years) - 1) * 100


def _find_nav_on_date(entries: List[Dict], target_date: datetime, tolerance_days: int = 7) -> Optional[float]:
    """Find NAV closest to target date within tolerance."""
    best = None
    best_diff = timedelta(days=tolerance_days + 1)
    for entry in entries:
        diff = abs(entry["date"] - target_date)
        if diff < best_diff:
            best = entry["nav"]
            best_diff = diff
    if best_diff.days <= tolerance_days:
        return best
    return None


def _is_direct_plan(scheme_name: str) -> bool:
    """Check if scheme name indicates Direct plan."""
    name_lower = scheme_name.lower()
    return "direct" in name_lower


def _detect_category(scheme_name: str, scheme_category: str) -> str:
    """Normalize category from API data."""
    return scheme_category if scheme_category else "Unknown"


def _is_shariah_ethical(scheme_name: str) -> bool:
    """Check if fund is Shariah/Ethical."""
    name_lower = scheme_name.lower()
    return any(kw in name_lower for kw in ["ethical", "shariah", "sharia"])


# ─── Input Models ────────────────────────────────────────────────────────────

class SearchFundsInput(BaseModel):
    """Input for searching mutual fund schemes."""
    model_config = ConfigDict(str_strip_whitespace=True)

    query: str = Field(..., description="Search query — fund name, AMC name, or category keyword (e.g., 'Tata Ethical', 'HDFC Flexi Cap', 'Nifty 50 Index')", min_length=2, max_length=200)
    direct_only: bool = Field(default=True, description="If true, return only Direct plan schemes (recommended — lower expense ratio)")
    growth_only: bool = Field(default=True, description="If true, return only Growth option schemes (recommended for long-term investing)")
    limit: int = Field(default=10, description="Maximum results to return", ge=1, le=50)

    @field_validator("query")
    @classmethod
    def validate_query(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Query cannot be empty")
        return v.strip()


class FundReturnsInput(BaseModel):
    """Input for calculating fund returns."""
    model_config = ConfigDict(str_strip_whitespace=True)

    scheme_code: int = Field(..., description="AMFI scheme code (get from india_mf_search)", ge=100000)
    periods: List[int] = Field(
        default=[1, 3, 5, 7, 10],
        description="Return periods in years to calculate (e.g., [1, 3, 5] for 1yr, 3yr, 5yr CAGR)",
        min_length=1, max_length=10
    )


class RollingReturnsInput(BaseModel):
    """Input for rolling return analysis."""
    model_config = ConfigDict(str_strip_whitespace=True)

    scheme_code: int = Field(..., description="AMFI scheme code", ge=100000)
    rolling_period_years: int = Field(default=3, description="Rolling window in years (e.g., 3 = 3-year rolling returns)", ge=1, le=10)


class CompareFundsInput(BaseModel):
    """Input for comparing multiple funds."""
    model_config = ConfigDict(str_strip_whitespace=True)

    scheme_codes: List[int] = Field(..., description="List of 2-5 AMFI scheme codes to compare", min_length=2, max_length=5)
    periods: List[int] = Field(
        default=[1, 3, 5],
        description="Return periods in years for comparison",
        min_length=1, max_length=5
    )


class SimulateSIPInput(BaseModel):
    """Input for SIP simulation."""
    model_config = ConfigDict(str_strip_whitespace=True)

    scheme_code: int = Field(..., description="AMFI scheme code to simulate SIP for", ge=100000)
    monthly_amount: float = Field(..., description="Monthly SIP amount in ₹ (e.g., 5000)", ge=100, le=10000000)
    years: int = Field(..., description="SIP duration in years", ge=1, le=30)
    step_up_percent: float = Field(default=0, description="Annual step-up % (e.g., 10 = increase SIP by 10% each year)", ge=0, le=50)


class SimulateSTPInput(BaseModel):
    """Input for STP simulation."""
    model_config = ConfigDict(str_strip_whitespace=True)

    scheme_code: int = Field(..., description="Target equity fund scheme code", ge=100000)
    lump_sum: float = Field(..., description="Lump sum amount in ₹ to deploy via STP", ge=10000)
    duration_months: int = Field(default=12, description="STP duration in months", ge=3, le=36)


class TaxHarvestInput(BaseModel):
    """Input for tax harvesting calculation."""
    model_config = ConfigDict(str_strip_whitespace=True)

    holdings: List[Dict[str, Any]] = Field(
        ...,
        description="List of holdings, each with: scheme_code (int), units (float), purchase_nav (float), purchase_date (DD-MM-YYYY string)"
    )
    ltcg_exemption: float = Field(default=125000, description="Annual LTCG exemption limit in ₹ (currently ₹1.25L)")


class CategoryTopInput(BaseModel):
    """Input for getting top funds in a category."""
    model_config = ConfigDict(str_strip_whitespace=True)

    category_keyword: str = Field(..., description="Category to search (e.g., 'flexi cap', 'large cap', 'mid cap', 'small cap', 'ELSS', 'index', 'liquid')", min_length=2)
    top_n: int = Field(default=5, description="Number of top funds to return", ge=1, le=20)
    period_years: int = Field(default=5, description="Period for ranking (e.g., 5 = rank by 5-year CAGR)", ge=1, le=10)


class SchemeCodeInput(BaseModel):
    """Input for single scheme code lookup."""
    model_config = ConfigDict(str_strip_whitespace=True)

    scheme_code: int = Field(..., description="AMFI scheme code", ge=100000)


# ─── Tools ───────────────────────────────────────────────────────────────────

@mcp.tool(
    name="india_mf_search",
    annotations={
        "title": "Search Indian Mutual Funds",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_search(params: SearchFundsInput) -> str:
    """Search for Indian mutual fund schemes by name, AMC, or category.

    Returns scheme codes, names, and fund house. Use scheme_code with other tools.
    Filters for Direct Growth plans by default (best for long-term investors).

    Args:
        params: Search parameters with query, direct_only, growth_only, limit

    Returns:
        Markdown table of matching funds with scheme codes, or error message.
    """
    try:
        data = await _make_api_request(f"mf/search?q={params.query}")

        if not data:
            return f"No funds found matching '{params.query}'. Try broader terms (e.g., 'Tata' instead of 'Tata Ethical Fund Direct Growth')."

        results = []
        for scheme in data:
            name = scheme.get("schemeName", "")
            code = scheme.get("schemeCode")

            if params.direct_only and not _is_direct_plan(name):
                continue
            if params.growth_only and "growth" not in name.lower():
                continue

            results.append({"code": code, "name": name})

            if len(results) >= params.limit:
                break

        if not results:
            return f"No Direct Growth funds found for '{params.query}'. Try setting direct_only=false to see Regular plans too."

        lines = [f"## Search Results: '{params.query}'", ""]
        lines.append(f"Found {len(results)} funds (Direct Growth):", )
        lines.append("")
        lines.append("| Scheme Code | Fund Name |")
        lines.append("|-------------|-----------|")
        for r in results:
            lines.append(f"| {r['code']} | {r['name']} |")
        lines.append("")
        lines.append("Use scheme_code with `india_mf_returns` or `india_mf_compare` for detailed analysis.")

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_nav",
    annotations={
        "title": "Get Latest NAV",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_nav(params: SchemeCodeInput) -> str:
    """Get latest NAV and basic info for a mutual fund scheme.

    Args:
        params: Scheme code input

    Returns:
        Fund name, latest NAV, date, fund house, and category.
    """
    try:
        data = await _get_nav_history(params.scheme_code)
        meta = data.get("meta", {})
        nav_data = data.get("data", [])

        if not nav_data:
            return f"No NAV data available for scheme {params.scheme_code}."

        latest = nav_data[0]  # API returns newest first

        lines = [
            f"## {meta.get('scheme_name', 'Unknown')}",
            "",
            f"- **Scheme Code**: {meta.get('scheme_code')}",
            f"- **Fund House**: {meta.get('fund_house', 'N/A')}",
            f"- **Category**: {meta.get('scheme_category', 'N/A')}",
            f"- **Type**: {meta.get('scheme_type', 'N/A')}",
            f"- **Latest NAV**: ₹{latest['nav']} (as of {latest['date']})",
            f"- **ISIN**: {meta.get('isin_growth', 'N/A')}",
            f"- **Data points**: {len(nav_data)} trading days of history",
        ]

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_returns",
    annotations={
        "title": "Calculate Fund Returns (CAGR)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_returns(params: FundReturnsInput) -> str:
    """Calculate CAGR returns for specified periods (1yr, 3yr, 5yr, etc.).

    Uses historical NAV data to compute actual point-to-point CAGR.
    Also calculates max drawdown and volatility.

    Args:
        params: Scheme code and list of periods in years

    Returns:
        Markdown table with CAGR for each period, plus risk metrics.
    """
    try:
        data = await _get_nav_history(params.scheme_code)
        meta = data.get("meta", {})
        entries = _parse_nav_data(data)

        if len(entries) < 30:
            return f"Insufficient data for scheme {params.scheme_code}. Only {len(entries)} data points available."

        latest_nav = entries[-1]["nav"]
        latest_date = entries[-1]["date"]

        lines = [
            f"## Returns: {meta.get('scheme_name', 'Unknown')}",
            f"**Latest NAV**: ₹{latest_nav:.2f} ({latest_date.strftime('%d-%b-%Y')})",
            "",
            "| Period | CAGR | Start NAV | Start Date |",
            "|--------|------|-----------|-----------|"
        ]

        for years in sorted(params.periods):
            target_date = latest_date - timedelta(days=years * 365)
            start_nav = _find_nav_on_date(entries, target_date)

            if start_nav:
                cagr = _calculate_cagr(start_nav, latest_nav, years)
                start_date_str = target_date.strftime("%d-%b-%Y")
                lines.append(f"| {years}Y | {cagr:.1f}% | ₹{start_nav:.2f} | ~{start_date_str} |")
            else:
                lines.append(f"| {years}Y | N/A (insufficient history) | - | - |")

        # Calculate risk metrics from last 3 years of daily returns
        recent_entries = entries[-756:]  # ~3 years of trading days
        if len(recent_entries) > 30:
            daily_returns = []
            for i in range(1, len(recent_entries)):
                ret = (recent_entries[i]["nav"] / recent_entries[i - 1]["nav"] - 1) * 100
                daily_returns.append(ret)

            # Max drawdown
            peak = recent_entries[0]["nav"]
            max_dd = 0
            for entry in recent_entries:
                if entry["nav"] > peak:
                    peak = entry["nav"]
                dd = (entry["nav"] - peak) / peak * 100
                if dd < max_dd:
                    max_dd = dd

            # Annualized volatility
            daily_vol = stdev(daily_returns) if len(daily_returns) > 1 else 0
            annual_vol = daily_vol * math.sqrt(252)

            lines.extend([
                "",
                "**Risk Metrics (last 3 years):**",
                f"- Max Drawdown: {max_dd:.1f}%",
                f"- Annualized Volatility: {annual_vol:.1f}%",
            ])

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_rolling_returns",
    annotations={
        "title": "Rolling Return Analysis",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_rolling_returns(params: RollingReturnsInput) -> str:
    """Calculate rolling returns to assess fund consistency.

    Shows min, max, average, median rolling returns and % of periods
    with positive returns. More reliable than point-to-point returns.

    Args:
        params: Scheme code and rolling period in years

    Returns:
        Rolling return statistics — min, max, avg, median, % positive periods.
    """
    try:
        data = await _get_nav_history(params.scheme_code)
        meta = data.get("meta", {})
        entries = _parse_nav_data(data)

        window_days = params.rolling_period_years * 252  # trading days

        if len(entries) < window_days + 50:
            return f"Insufficient history for {params.rolling_period_years}-year rolling analysis. Need ~{window_days + 50} trading days, have {len(entries)}."

        rolling_returns = []
        for i in range(window_days, len(entries)):
            start_nav = entries[i - window_days]["nav"]
            end_nav = entries[i]["nav"]
            cagr = _calculate_cagr(start_nav, end_nav, params.rolling_period_years)
            rolling_returns.append(cagr)

        if not rolling_returns:
            return "Could not calculate rolling returns."

        rolling_returns.sort()
        positive_pct = sum(1 for r in rolling_returns if r > 0) / len(rolling_returns) * 100
        above_10_pct = sum(1 for r in rolling_returns if r >= 10) / len(rolling_returns) * 100
        above_12_pct = sum(1 for r in rolling_returns if r >= 12) / len(rolling_returns) * 100

        avg_ret = mean(rolling_returns)
        median_ret = rolling_returns[len(rolling_returns) // 2]
        min_ret = rolling_returns[0]
        max_ret = rolling_returns[-1]

        # Percentiles
        p25 = rolling_returns[int(len(rolling_returns) * 0.25)]
        p75 = rolling_returns[int(len(rolling_returns) * 0.75)]

        lines = [
            f"## Rolling {params.rolling_period_years}Y Returns: {meta.get('scheme_name', 'Unknown')}",
            f"Based on {len(rolling_returns)} rolling periods",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            f"| Minimum | {min_ret:.1f}% |",
            f"| 25th Percentile | {p25:.1f}% |",
            f"| Median | {median_ret:.1f}% |",
            f"| Average | {avg_ret:.1f}% |",
            f"| 75th Percentile | {p75:.1f}% |",
            f"| Maximum | {max_ret:.1f}% |",
            "",
            "**Consistency:**",
            f"- Positive returns: {positive_pct:.0f}% of periods",
            f"- Returns ≥10%: {above_10_pct:.0f}% of periods",
            f"- Returns ≥12%: {above_12_pct:.0f}% of periods",
            "",
            f"**Interpretation**: {'Highly consistent' if positive_pct > 90 else 'Consistent' if positive_pct > 75 else 'Moderate consistency' if positive_pct > 60 else 'Inconsistent — higher risk'}. "
            f"{'Strong compounder' if avg_ret > 12 else 'Decent performer' if avg_ret > 8 else 'Below average'}."
        ]

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_compare",
    annotations={
        "title": "Compare Multiple Funds",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_compare(params: CompareFundsInput) -> str:
    """Side-by-side comparison of 2-5 funds on returns and risk.

    Args:
        params: List of scheme codes and comparison periods

    Returns:
        Comparison table with CAGR, drawdown, and volatility for each fund.
    """
    try:
        funds_data = []
        for code in params.scheme_codes:
            data = await _get_nav_history(code)
            entries = _parse_nav_data(data)
            meta = data.get("meta", {})
            funds_data.append({
                "code": code,
                "name": meta.get("scheme_name", str(code)),
                "category": meta.get("scheme_category", "N/A"),
                "entries": entries
            })

        # Build comparison header
        short_names = []
        for f in funds_data:
            # Shorten name for table readability
            name = f["name"].replace(" - Direct Plan", "").replace(" - Growth", "").replace(" Direct Growth", "")
            if len(name) > 35:
                name = name[:32] + "..."
            short_names.append(name)

        lines = [
            "## Fund Comparison",
            "",
            "| Metric | " + " | ".join(short_names) + " |",
            "|--------" + "|--------" * len(funds_data) + "|"
        ]

        # Category row
        cats = [f["category"] for f in funds_data]
        lines.append("| Category | " + " | ".join(cats) + " |")

        # Returns for each period
        for years in sorted(params.periods):
            row_values = []
            for f in funds_data:
                entries = f["entries"]
                if entries:
                    latest_date = entries[-1]["date"]
                    latest_nav = entries[-1]["nav"]
                    target_date = latest_date - timedelta(days=years * 365)
                    start_nav = _find_nav_on_date(entries, target_date)
                    if start_nav:
                        cagr = _calculate_cagr(start_nav, latest_nav, years)
                        row_values.append(f"{cagr:.1f}%")
                    else:
                        row_values.append("N/A")
                else:
                    row_values.append("N/A")
            lines.append(f"| {years}Y CAGR | " + " | ".join(row_values) + " |")

        # Max drawdown (3yr)
        dd_values = []
        vol_values = []
        for f in funds_data:
            entries = f["entries"][-756:]
            if len(entries) > 30:
                peak = entries[0]["nav"]
                max_dd = 0
                for entry in entries:
                    if entry["nav"] > peak:
                        peak = entry["nav"]
                    dd = (entry["nav"] - peak) / peak * 100
                    if dd < max_dd:
                        max_dd = dd
                dd_values.append(f"{max_dd:.1f}%")

                daily_rets = [(entries[i]["nav"] / entries[i - 1]["nav"] - 1) * 100
                              for i in range(1, len(entries))]
                vol = stdev(daily_rets) * math.sqrt(252) if len(daily_rets) > 1 else 0
                vol_values.append(f"{vol:.1f}%")
            else:
                dd_values.append("N/A")
                vol_values.append("N/A")

        lines.append(f"| Max Drawdown (3Y) | " + " | ".join(dd_values) + " |")
        lines.append(f"| Volatility (3Y) | " + " | ".join(vol_values) + " |")

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_simulate_sip",
    annotations={
        "title": "SIP Simulator",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_simulate_sip(params: SimulateSIPInput) -> str:
    """Simulate SIP returns using actual historical NAV data.

    Shows what a monthly SIP would have grown to based on real fund performance.
    Supports step-up SIP (annual increase in SIP amount).

    Args:
        params: Scheme code, monthly amount, years, optional step-up %

    Returns:
        SIP simulation with total invested, current value, returns, and XIRR.
    """
    try:
        data = await _get_nav_history(params.scheme_code)
        meta = data.get("meta", {})
        entries = _parse_nav_data(data)

        if not entries:
            return "No NAV data available."

        latest_date = entries[-1]["date"]
        start_date = latest_date - timedelta(days=params.years * 365)

        # Filter entries to SIP period
        sip_entries = [e for e in entries if e["date"] >= start_date]
        if len(sip_entries) < 12:
            return f"Insufficient data for {params.years}-year SIP simulation. Fund may not have enough history."

        # Simulate monthly SIP
        total_invested = 0.0
        total_units = 0.0
        monthly_sip = params.monthly_amount
        current_month = -1
        current_year = -1
        sip_year = 0
        investments = []  # For XIRR-like calculation

        for entry in sip_entries:
            month = entry["date"].month
            year = entry["date"].year

            if month != current_month or year != current_year:
                # New month — invest
                if year != current_year and current_year != -1:
                    sip_year += 1
                    if params.step_up_percent > 0:
                        monthly_sip = params.monthly_amount * ((1 + params.step_up_percent / 100) ** sip_year)

                units_bought = monthly_sip / entry["nav"]
                total_units += units_bought
                total_invested += monthly_sip
                investments.append({"date": entry["date"], "amount": -monthly_sip})
                current_month = month
                current_year = year

        # Current value
        current_nav = entries[-1]["nav"]
        current_value = total_units * current_nav
        absolute_return = current_value - total_invested
        absolute_return_pct = (absolute_return / total_invested) * 100 if total_invested > 0 else 0

        # Simple annualized return approximation
        avg_investment_period = params.years / 2  # Average money was invested for half the period
        if avg_investment_period > 0 and total_invested > 0:
            approx_cagr = _calculate_cagr(total_invested, current_value, avg_investment_period)
        else:
            approx_cagr = 0

        step_up_note = f" (with {params.step_up_percent}% annual step-up)" if params.step_up_percent > 0 else ""

        lines = [
            f"## SIP Simulation: {meta.get('scheme_name', 'Unknown')}",
            f"**Period**: Last {params.years} years | **Monthly SIP**: ₹{params.monthly_amount:,.0f}{step_up_note}",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            f"| Total Invested | ₹{total_invested:,.0f} |",
            f"| Current Value | ₹{current_value:,.0f} |",
            f"| Profit/Loss | ₹{absolute_return:,.0f} |",
            f"| Absolute Return | {absolute_return_pct:.1f}% |",
            f"| Approx. Annualized Return | {approx_cagr:.1f}% |",
            f"| Total Units | {total_units:.3f} |",
            f"| Avg NAV Bought | ₹{(total_invested / total_units):.2f} |" if total_units > 0 else "",
            f"| Current NAV | ₹{current_nav:.2f} |",
        ]

        if params.step_up_percent > 0:
            lines.extend([
                "",
                f"**Step-up impact**: Final monthly SIP was ₹{monthly_sip:,.0f} (started at ₹{params.monthly_amount:,.0f})."
            ])

        lines.extend([
            "",
            "*Note: This uses actual historical NAV data. Past performance does not guarantee future returns.*"
        ])

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_simulate_stp",
    annotations={
        "title": "STP Simulator",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_simulate_stp(params: SimulateSTPInput) -> str:
    """Simulate STP — deploying a lump sum gradually via monthly transfers.

    Compares STP vs lump sum investment over the same period.

    Args:
        params: Target fund scheme code, lump sum amount, STP duration in months

    Returns:
        STP vs lump sum comparison with final values.
    """
    try:
        data = await _get_nav_history(params.scheme_code)
        meta = data.get("meta", {})
        entries = _parse_nav_data(data)

        if not entries:
            return "No NAV data available."

        latest_date = entries[-1]["date"]
        start_date = latest_date - timedelta(days=params.duration_months * 30 + 30)

        stp_entries = [e for e in entries if e["date"] >= start_date]
        if len(stp_entries) < params.duration_months:
            return f"Insufficient data for {params.duration_months}-month STP simulation."

        monthly_transfer = params.lump_sum / params.duration_months

        # STP simulation
        stp_units = 0.0
        stp_invested = 0.0
        current_month = -1
        months_done = 0

        # Lump sum simulation
        lump_nav = stp_entries[0]["nav"]
        lump_units = params.lump_sum / lump_nav

        for entry in stp_entries:
            if entry["date"].month != current_month and months_done < params.duration_months:
                stp_units += monthly_transfer / entry["nav"]
                stp_invested += monthly_transfer
                current_month = entry["date"].month
                months_done += 1

        current_nav = entries[-1]["nav"]
        stp_value = stp_units * current_nav
        lump_value = lump_units * current_nav

        lines = [
            f"## STP Simulation: {meta.get('scheme_name', 'Unknown')}",
            f"**Lump Sum**: ₹{params.lump_sum:,.0f} | **STP Duration**: {params.duration_months} months",
            "",
            "| Metric | STP | Lump Sum |",
            "|--------|-----|----------|",
            f"| Amount Deployed | ₹{stp_invested:,.0f} | ₹{params.lump_sum:,.0f} |",
            f"| Units Bought | {stp_units:.3f} | {lump_units:.3f} |",
            f"| Avg Buy NAV | ₹{(stp_invested / stp_units):.2f} | ₹{lump_nav:.2f} |" if stp_units > 0 else "",
            f"| Current Value | ₹{stp_value:,.0f} | ₹{lump_value:,.0f} |",
            f"| Return | {((stp_value / stp_invested - 1) * 100):.1f}% | {((lump_value / params.lump_sum - 1) * 100):.1f}% |",
            f"| **Winner** | {'✓ STP' if stp_value > lump_value else ''} | {'✓ Lump Sum' if lump_value >= stp_value else ''} |",
            "",
            "*In rising markets, lump sum usually wins. In volatile/falling markets, STP wins by averaging down.*"
        ]

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_tax_harvest",
    annotations={
        "title": "Tax Harvesting Calculator",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def india_mf_tax_harvest(params: TaxHarvestInput) -> str:
    """Calculate LTCG harvesting opportunity within ₹1.25L annual exemption.

    India has no wash sale rules — you can sell and immediately rebuy
    the same fund to book tax-free gains within the exemption limit.

    Args:
        params: List of holdings with scheme_code, units, purchase_nav, purchase_date

    Returns:
        Harvest recommendation — which holdings to sell, estimated tax saved.
    """
    try:
        results = []
        total_ltcg = 0.0
        total_stcg = 0.0

        for holding in params.holdings:
            code = holding.get("scheme_code")
            units = float(holding.get("units", 0))
            purchase_nav = float(holding.get("purchase_nav", 0))
            purchase_date_str = holding.get("purchase_date", "")

            try:
                purchase_date = datetime.strptime(purchase_date_str, DATE_FORMAT)
            except ValueError:
                results.append({"code": code, "error": f"Invalid date format: {purchase_date_str}"})
                continue

            data = await _get_nav_history(code)
            entries = _parse_nav_data(data)
            meta = data.get("meta", {})

            if not entries:
                continue

            current_nav = entries[-1]["nav"]
            gain_per_unit = current_nav - purchase_nav
            total_gain = gain_per_unit * units
            holding_days = (entries[-1]["date"] - purchase_date).days
            is_ltcg = holding_days > 365

            if is_ltcg:
                total_ltcg += total_gain
            else:
                total_stcg += total_gain

            results.append({
                "name": meta.get("scheme_name", str(code)),
                "units": units,
                "purchase_nav": purchase_nav,
                "current_nav": current_nav,
                "gain": total_gain,
                "holding_days": holding_days,
                "is_ltcg": is_ltcg
            })

        # Harvesting recommendation
        harvestable = min(total_ltcg, params.ltcg_exemption) if total_ltcg > 0 else 0
        tax_saved = harvestable * 0.125  # 12.5% LTCG tax

        lines = [
            "## Tax Harvesting Analysis",
            "",
            "| Fund | Gain/Loss | Type | Holding Period |",
            "|------|-----------|------|---------------|"
        ]

        for r in results:
            if "error" in r:
                lines.append(f"| Code {r['code']} | Error: {r['error']} | - | - |")
            else:
                gain_str = f"₹{r['gain']:+,.0f}"
                type_str = "LTCG" if r["is_ltcg"] else "STCG"
                lines.append(f"| {r['name'][:40]} | {gain_str} | {type_str} | {r['holding_days']} days |")

        lines.extend([
            "",
            f"**Total LTCG**: ₹{total_ltcg:,.0f}",
            f"**Total STCG**: ₹{total_stcg:,.0f}",
            f"**Harvestable within ₹{params.ltcg_exemption/100000:.2f}L exemption**: ₹{harvestable:,.0f}",
            f"**Estimated tax saved**: ₹{tax_saved:,.0f} (at 12.5% LTCG rate)",
            "",
            "**Action**: Sell units with LTCG up to ₹1.25L, immediately rebuy the same fund. India has no wash sale rules — this is legal and widely used.",
            "",
            "*Based on current NAV. Execute before March 31 for current FY benefit.*"
        ])

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_category_top",
    annotations={
        "title": "Top Funds by Category",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_category_top(params: CategoryTopInput) -> str:
    """Find top-performing funds in a category ranked by CAGR.

    Searches for funds matching the category keyword, calculates returns,
    and ranks them. Only Direct Growth plans included.

    Args:
        params: Category keyword, number of top funds, ranking period

    Returns:
        Ranked table of top funds with returns and risk metrics.
    """
    try:
        # Search for funds in this category
        search_data = await _make_api_request(f"mf/search?q={params.category_keyword}")

        if not search_data:
            return f"No funds found for category '{params.category_keyword}'."

        # Filter Direct Growth only
        candidates = []
        for scheme in search_data:
            name = scheme.get("schemeName", "")
            code = scheme.get("schemeCode")
            if _is_direct_plan(name) and "growth" in name.lower():
                candidates.append({"code": code, "name": name})

        if not candidates:
            return f"No Direct Growth funds found for '{params.category_keyword}'."

        # Limit candidates to avoid too many API calls
        candidates = candidates[:30]

        # Calculate returns for each
        fund_returns = []
        for cand in candidates:
            try:
                data = await _get_nav_history(cand["code"])
                entries = _parse_nav_data(data)
                if len(entries) < params.period_years * 200:  # Need enough history
                    continue

                latest_nav = entries[-1]["nav"]
                latest_date = entries[-1]["date"]
                target_date = latest_date - timedelta(days=params.period_years * 365)
                start_nav = _find_nav_on_date(entries, target_date)

                if start_nav:
                    cagr = _calculate_cagr(start_nav, latest_nav, params.period_years)
                    fund_returns.append({
                        "code": cand["code"],
                        "name": cand["name"],
                        "cagr": cagr,
                        "category": data.get("meta", {}).get("scheme_category", "N/A")
                    })
            except Exception:
                continue

        if not fund_returns:
            return f"Could not calculate returns for any '{params.category_keyword}' funds over {params.period_years} years."

        # Sort by CAGR descending
        fund_returns.sort(key=lambda x: x["cagr"], reverse=True)
        top = fund_returns[:params.top_n]

        lines = [
            f"## Top {params.category_keyword.title()} Funds ({params.period_years}Y CAGR)",
            "",
            "| Rank | Fund | Scheme Code | {0}Y CAGR |".format(params.period_years),
            "|------|------|-------------|----------|"
        ]

        for i, f in enumerate(top, 1):
            name = f["name"].replace(" - Direct Plan", "").replace(" - Growth", "").replace(" Direct Growth", "")
            if len(name) > 40:
                name = name[:37] + "..."
            lines.append(f"| {i} | {name} | {f['code']} | {f['cagr']:.1f}% |")

        lines.extend([
            "",
            f"*Ranked by {params.period_years}-year CAGR. Use `india_mf_returns` or `india_mf_rolling_returns` for deeper analysis of specific funds.*",
            f"*Only Direct Growth plans with sufficient history shown. Screened {len(candidates)} candidates.*"
        ])

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="india_mf_shariah",
    annotations={
        "title": "Shariah/Ethical Fund Finder",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def india_mf_shariah(params: Optional[SchemeCodeInput] = None) -> str:
    """Find all Shariah-compliant and Ethical mutual funds available in India.

    Searches for funds with 'ethical' or 'shariah' in their name.
    Returns Direct Growth plans with latest NAV and available return data.

    Args:
        params: Optional — if scheme_code provided, shows details for that specific ethical fund.

    Returns:
        List of Shariah/Ethical funds with NAV and basic performance data.
    """
    try:
        # Search for ethical/shariah funds
        ethical_funds = []

        for keyword in ["ethical", "shariah"]:
            search_data = await _make_api_request(f"mf/search?q={keyword}")
            if search_data:
                for scheme in search_data:
                    name = scheme.get("schemeName", "")
                    code = scheme.get("schemeCode")
                    if _is_direct_plan(name) and "growth" in name.lower():
                        if not any(f["code"] == code for f in ethical_funds):
                            ethical_funds.append({"code": code, "name": name})

        if not ethical_funds:
            return "No Shariah/Ethical funds found. The Indian MF universe has very few — Tata Ethical Fund and Quantum Ethical Fund are the main options."

        lines = [
            "## Shariah / Ethical Funds (India)",
            "Direct Growth plans only",
            ""
        ]

        for fund in ethical_funds:
            try:
                data = await _get_nav_history(fund["code"])
                meta = data.get("meta", {})
                entries = _parse_nav_data(data)

                if not entries:
                    continue

                latest_nav = entries[-1]["nav"]
                latest_date = entries[-1]["date"]

                # Calculate returns if enough data
                returns_str = ""
                for years in [1, 3, 5]:
                    target_date = latest_date - timedelta(days=years * 365)
                    start_nav = _find_nav_on_date(entries, target_date)
                    if start_nav:
                        cagr = _calculate_cagr(start_nav, latest_nav, years)
                        returns_str += f" | {years}Y: {cagr:.1f}%"

                lines.extend([
                    f"### {meta.get('scheme_name', fund['name'])}",
                    f"- **Scheme Code**: {fund['code']}",
                    f"- **Fund House**: {meta.get('fund_house', 'N/A')}",
                    f"- **Category**: {meta.get('scheme_category', 'N/A')}",
                    f"- **Latest NAV**: ₹{latest_nav:.2f} ({latest_date.strftime('%d-%b-%Y')})",
                    f"- **Returns (CAGR)**:{returns_str}" if returns_str else "",
                    ""
                ])
            except Exception:
                lines.append(f"### {fund['name']} (Code: {fund['code']}) — Data unavailable")
                lines.append("")

        lines.extend([
            "---",
            "**Note**: India has very few Shariah-compliant MFs. Tata Ethical Fund (since 1996, TASIS certified) is the oldest.",
            "For Shariah portfolio construction, see india-mutual-fund-advisor Step 11.",
            "For Shariah model portfolios, see references/model-portfolios.md."
        ])

        return "\n".join(lines)

    except Exception as e:
        return _handle_api_error(e)


if __name__ == "__main__":
    mcp.run()
