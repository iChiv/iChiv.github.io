#!/usr/bin/env python3
import re
import os
import subprocess
from html import unescape

def extract_media_and_links(html_file, project_name):
    """Extract images, links, and videos from HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract images
    images = re.findall(r'<img[^>]+src="(https://redox\.games/wp-content/uploads/[^"]+)"[^>]*>', html)
    
    # Extract external links (itch.io, youtube, etc)
    links = re.findall(r'<a[^>]+href="(https?://(?:itch\.io|youtube\.com|youtu\.be|vimeo\.com)[^"]*)"[^>]*>([^<]*)</a>', html)
    
    # Extract iframe videos
    videos = re.findall(r'<iframe[^>]+src="(https?://(?:www\.)?youtube\.com/embed/([^"?]+)[^"]*)"', html)
    
    # Extract title
    title_match = re.search(r'<h1[^>]*class="entry-title"[^>]*>([^<]+)</h1>', html)
    title = unescape(title_match.group(1).strip()) if title_match else project_name
    
    return {
        'title': title,
        'images': images,
        'links': links,
        'videos': videos
    }

# Process all projects
projects = {
    'finite-space': '/tmp/finite-space.html',
    'project-catch': '/tmp/project-catch.html',
    'cute-td': '/tmp/cute-td.html',
    'mon-ssenger': '/tmp/mon-ssenger.html',
    'dice-adventure': '/tmp/dice-adventure.html',
    'repair-below': '/tmp/repair-below.html',
    'mortise-mirage': '/tmp/mortise-mirage.html',
    'findy-hunter': '/tmp/findy-hunter.html',
    'death-stranding': '/tmp/death-stranding.html',
    'ring-fit': '/tmp/ring-fit.html',
    'slay-the-spire': '/tmp/slay-the-spire.html',
}

# Create download directory
os.makedirs('assets/images/projects', exist_ok=True)
os.makedirs('assets/images/xr', exist_ok=True)
os.makedirs('assets/images/reviews', exist_ok=True)

all_downloads = []

for name, path in projects.items():
    print(f"\n{'='*60}")
    print(f"Processing: {name}")
    print('='*60)
    
    data = extract_media_and_links(path, name)
    print(f"Title: {data['title']}")
    
    # Determine category
    if name in ['finite-space', 'project-catch', 'cute-td', 'mon-ssenger', 'dice-adventure']:
        category = 'projects'
    elif name in ['repair-below', 'mortise-mirage', 'findy-hunter']:
        category = 'xr'
    else:
        category = 'reviews'
    
    # Download images
    print(f"\nImages ({len(data['images'])}):")
    for i, img_url in enumerate(data['images'][:10], 1):  # Limit to 10 images per project
        # Get file extension
        ext = img_url.split('.')[-1].split('?')[0]
        if ext not in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
            ext = 'jpg'
        
        filename = f"{name}-{i}.{ext}"
        filepath = f"assets/images/{category}/{filename}"
        
        print(f"  {i}. {img_url}")
        all_downloads.append((img_url, filepath))
    
    # Links
    print(f"\nLinks ({len(data['links'])}):")
    for url, text in data['links']:
        print(f"  - {text}: {url}")
    
    # Videos
    print(f"\nVideos ({len(data['videos'])}):")
    for url, video_id in data['videos']:
        print(f"  - YouTube: {video_id}")

print(f"\n\nTotal images to download: {len(all_downloads)}")

# Save download list
with open('download_list.txt', 'w') as f:
    for url, path in all_downloads:
        f.write(f"{url} {path}\n")

print("\nDownload list saved to download_list.txt")
