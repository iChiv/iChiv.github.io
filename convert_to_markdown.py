#!/usr/bin/env python3
import re
import os
from html.parser import HTMLParser
from html import unescape

class ContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_entry_content = False
        self.content = []
        self.current_tag = None
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer'}
        self.in_skip = False
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        
        # Check if entering entry-content div
        for name, value in attrs:
            if name == 'class' and 'entry-content' in value:
                self.in_entry_content = True
                return
        
        if tag in self.skip_tags:
            self.in_skip = True
            
        if self.in_entry_content and not self.in_skip:
            if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                self.content.append('\n\n## ')
            elif tag == 'p':
                self.content.append('\n\n')
            elif tag == 'br':
                self.content.append('\n')
            elif tag == 'strong' or tag == 'b':
                self.content.append('**')
            elif tag == 'em' or tag == 'i':
                self.content.append('*')
            elif tag == 'a':
                for name, value in attrs:
                    if name == 'href':
                        self.content.append('[')
            elif tag == 'img':
                for name, value in attrs:
                    if name == 'src':
                        alt = ''
                        for n, v in attrs:
                            if n == 'alt':
                                alt = v
                        self.content.append(f'\n\n![{alt}]({value})\n\n')
            elif tag == 'ul':
                self.content.append('\n\n')
            elif tag == 'ol':
                self.content.append('\n\n')
            elif tag == 'li':
                self.content.append('\n- ')
            elif tag == 'blockquote':
                self.content.append('\n\n> ')
            elif tag == 'code':
                self.content.append('`')
            elif tag == 'pre':
                self.content.append('\n\n```\n')
                
    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_skip = False
            
        if self.in_entry_content and not self.in_skip:
            if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                self.content.append('\n\n')
            elif tag == 'strong' or tag == 'b':
                self.content.append('**')
            elif tag == 'em' or tag == 'i':
                self.content.append('*')
            elif tag == 'a':
                self.content.append(']()')
            elif tag == 'code':
                self.content.append('`')
            elif tag == 'pre':
                self.content.append('\n```\n')
                
        if tag == 'div' and self.in_entry_content:
            # Check if we're leaving entry-content
            pass  # We'll handle this differently
            
    def handle_data(self, data):
        if self.in_entry_content and not self.in_skip:
            cleaned = data.strip()
            if cleaned:
                self.content.append(data)
                
    def get_content(self):
        result = ''.join(self.content)
        # Clean up extra whitespace
        result = re.sub(r'\n{3,}', '\n\n', result)
        result = re.sub(r' {2,}', ' ', result)
        return result.strip()

def extract_title(html):
    """Extract title from HTML"""
    match = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
    if match:
        return unescape(match.group(1).strip())
    return "Untitled"

def extract_content(html_file):
    """Extract content from HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    title = extract_title(html)
    parser = ContentExtractor()
    parser.feed(html)
    content = parser.get_content()
    
    return title, content

def create_markdown_file(output_file, title, content, category, date=None, layout='project'):
    """Create a markdown file with front matter"""
    front_matter = f"""---
title: "{title}"
layout: {layout}
category: {category}
"""
    if date:
        front_matter += f"date: {date}\n"
    front_matter += "---\n\n"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(front_matter + content)
    
    print(f"Created: {output_file}")

# Process About page
title, content = extract_content('/tmp/about.html')
create_markdown_file('_pages/about.md', title, content, 'About', layout='page')

# Process Games
games = [
    ('finite-space', 'Finite Space', '2024-01-02'),
    ('project-catch', 'Project Catch', '2022-08-07'),
    ('cute-tower-defense', 'Cute Tower Defense', '2023-09-01'),
    ('mon-ssenger', 'Mon-ssenger', '2022-08-30'),
    ('dice-adventure', 'Dice Adventure', '2022-09-02'),
    ('other-games', 'Other Games', '2021-03-19'),
]

for slug, expected_title, date in games:
    title, content = extract_content(f'/tmp/{slug}.html')
    create_markdown_file(f'_games/{date}-{slug}.md', title, content, 'Games', date)

# Process XR
xr_projects = [
    ('repair-below', 'Repair Below From Above', '2022-09-01'),
    ('mortise-mirage', 'Mortise Mirage', '2024-03-06'),
    ('findy-hunter', 'Findy Hunter', '2024-01-04'),
]

for slug, expected_title, date in xr_projects:
    title, content = extract_content(f'/tmp/{slug}.html')
    create_markdown_file(f'_xr/{date}-{slug}.md', title, content, 'XR', date)

# Process Reviews
reviews = [
    ('death-stranding', 'Death Stranding', '2022-09-07'),
    ('ring-fit-adventure', 'Ring Fit Adventure', '2022-09-07'),
    ('slay-the-spire', 'Slay the Spire', '2022-09-07'),
]

for slug, expected_title, date in reviews:
    title, content = extract_content(f'/tmp/{slug}.html')
    create_markdown_file(f'_reviews/{date}-{slug}.md', title, content, 'Reviews', date)

print("\nAll files created!")
