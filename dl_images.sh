#!/bin/bash
# Download all images from redox.games

mkdir -p assets/images/projects assets/images/xr assets/images/reviews

# Avatar
curl -sL "https://redox.games/wp-content/uploads/2023/10/88380A4E-8ABB-42B0-887B-915DBE379E43-11929-0000093BA373D759_tmp.jpg" -o assets/images/avatar.jpg

# Finite Space
curl -sL "https://redox.games/wp-content/uploads/2024/01/l5XLYt-825x510.png" -o assets/images/projects/finite-space-cover.png

# Cute Tower Defense  
curl -sL "https://redox.games/wp-content/uploads/2024/01/l5XLYt-825x510.png" -o assets/images/projects/cute-td.png

# Dice Adventure
curl -sL "https://redox.games/wp-content/uploads/2022/09/9453-825x510.jpg" -o assets/images/projects/dice-adventure.jpg

# Death Stranding
curl -sL "https://redox.games/wp-content/uploads/2022/08/DS_wide-2560x1440-c3d7bbf8ee36dd025610088381a5235a-825x510.jpg" -o assets/images/reviews/death-stranding.jpg

# Findy Hunter
curl -sL "https://redox.games/wp-content/uploads/2024/01/2-1024x574.jpg" -o assets/images/xr/findy-hunter.jpg

echo "Images downloaded"
ls -la assets/images/
