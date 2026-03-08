#!/bin/bash
# Download all images from redox.games

BASE="https://redox.games/wp-content/uploads"

# Avatar
curl -sL "https://redox.games/wp-content/uploads/2023/10/88380A4E-8ABB-42B0-887B-915DBE379E43-11929-0000093BA373D759_tmp.jpg" -o assets/images/avatar.jpg

# Games images
curl -sL "$BASE/2024/01/finite-space-cover.png" -o assets/images/projects/finite-space.jpg 2>/dev/null || echo "No finite-space image"
curl -sL "$BASE/2022/08/project-catch.png" -o assets/images/projects/project-catch.jpg 2>/dev/null || echo "No project-catch image"
curl -sL "$BASE/2023/09/cute-td.png" -o assets/images/projects/cute-tower-defense.jpg 2>/dev/null || echo "No cute-td image"
curl -sL "$BASE/2022/08/mon-ssenger.png" -o assets/images/projects/mon-ssenger.jpg 2>/dev/null || echo "No mon-ssenger image"

# XR images
curl -sL "$BASE/2022/09/repair-below.png" -o assets/images/xr/repair-below.jpg 2>/dev/null || echo "No repair-below image"
curl -sL "$BASE/2024/03/mortise-mirage.png" -o assets/images/xr/mortise-mirage.jpg 2>/dev/null || echo "No mortise-mirage image"
curl -sL "$BASE/2024/01/findy-hunter.png" -o assets/images/xr/findy-hunter.jpg 2>/dev/null || echo "No findy-hunter image"

echo "Image download attempt complete"
ls -la assets/images/
ls -la assets/images/projects/ 2>/dev/null || echo "No project images"
ls -la assets/images/xr/ 2>/dev/null || echo "No XR images"
