#!/bin/bash
# Run this from the wealth-management-india folder
# Prerequisites: git installed, GitHub CLI (gh) installed and authenticated

set -e

echo "Creating GitHub repo..."
gh repo create wealth-management-india --public --description "India Wealth Management Plugin for Claude Cowork — 7 financial advisory skills + MCP server for live mutual fund data" --source . --push

echo ""
echo "Done! Your repo is live at:"
echo "https://github.com/$(gh api user --jq .login)/wealth-management-india"
