#!/bin/bash
# Script to fetch content from redox.games

BASE_URL="https://redox.games/index.php"

# Create directories
mkdir -p _games _xr _reviews

# Fetch About page content
echo "Fetching About..."
curl -sL "${BASE_URL}/about/" > /tmp/about.html

# Fetch Games
echo "Fetching Games..."
curl -sL "${BASE_URL}/2024/01/02/finite-space/" > /tmp/finite-space.html
curl -sL "${BASE_URL}/2022/08/07/project-catch/" > /tmp/project-catch.html
curl -sL "${BASE_URL}/2023/09/01/cute-tower-defense/" > /tmp/cute-tower-defense.html
curl -sL "${BASE_URL}/2022/08/30/mon-ssenger/" > /tmp/mon-ssenger.html
curl -sL "${BASE_URL}/2022/09/02/dice-adventure/" > /tmp/dice-adventure.html
curl -sL "${BASE_URL}/2021/03/19/other-games/" > /tmp/other-games.html

# Fetch XR
echo "Fetching XR..."
curl -sL "${BASE_URL}/2022/09/01/repair-below-from-above/" > /tmp/repair-below.html
curl -sL "${BASE_URL}/2024/03/06/mortise-mirage/" > /tmp/mortise-mirage.html
curl -sL "${BASE_URL}/2024/01/04/findy-hunter/" > /tmp/findy-hunter.html

# Fetch Reviews
echo "Fetching Reviews..."
curl -sL "${BASE_URL}/2022/09/07/death-stranding/" > /tmp/death-stranding.html
curl -sL "${BASE_URL}/2022/09/07/ring-fit-adventure/" > /tmp/ring-fit-adventure.html
curl -sL "${BASE_URL}/2022/09/07/slay-the-spire/" > /tmp/slay-the-spire.html

echo "Done fetching HTML files"
