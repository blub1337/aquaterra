#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final optimization: 
1. Use best image (326 KB) for HERO
2. Add missing top images to galleries
3. Optimize CSS for new images
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("FINAL OPTIMIZATION")
print("=" * 80)

# 1. Upgrade HERO to largest image (326 KB)
old_hero = "506986521_9911849908922104_1623314177700703878_n.jpg"  # 303 KB
new_hero = "506653046_9911850618922033_661776978636202946_n.jpg"  # 326 KB

if old_hero in content:
    content = content.replace(old_hero, new_hero)
    print(f"[OK] HERO upgraded: {old_hero[:40]}... -> {new_hero[:40]}...")
else:
    print(f"[--] Old hero not found: {old_hero[:40]}...")

# 2. Add missing large images to gallery
missing_images = [
    "505947241_9910989592341469_7562819216884758934_n.jpg",  # 286 KB - Terrace
    "505828493_9910989472341481_3879326001581608062_n.jpg",  # 253 KB - Food
    "506338969_9911464522293976_9065926674286702476_n.jpg",  # 242 KB - Food
    "506531577_9910989595674802_731187341473502969_n.jpg",  # 188 KB - Interior
]

# Find the Premium Gallery section and add more items
premium_gallery_pattern = r'(<section id="premium-gallery".*?<div class="gallery-grid">)(.*?)(</div>.*?</section>)'
match = re.search(premium_gallery_pattern, content, re.DOTALL)

if match:
    before_grid = match.group(1)
    grid_content = match.group(2)
    after_grid = match.group(3)
    
    # Count existing items in premium gallery
    existing_items = len(re.findall(r'<div class="gallery-item', grid_content))
    print(f"\nPremium Gallery has {existing_items} items")
    
    # Add 2 more items if needed
    if existing_items < 6:
        new_items = ""
        for img in missing_images[:2]:
            new_items += f'\n                <div class="gallery-item reveal" style="background-image: url(\'images/{img}\');"></div>'
        
        grid_content = grid_content.rstrip() + new_items + "\n            "
        
        # Replace in content
        new_section = before_grid + grid_content + after_grid
        content = content[:match.start()] + new_section + content[match.end():]
        print(f"[OK] Added 2 images to Premium Gallery")
else:
    print("[--] Premium Gallery section not found")

# 3. Update Social Gallery with better images
social_missing = [
    "510399090_9978560588917702_5067114327253013055_n.jpg",  # 99 KB
    "506531577_9910989595674802_731187341473502969_n.jpg",  # 188 KB
]

social_pattern = r'(<section id="social".*?<div class="gallery-grid">)(.*?)(</div>.*?</section>)'
match = re.search(social_pattern, content, re.DOTALL)

if match:
    before_grid = match.group(1)
    grid_content = match.group(2)
    after_grid = match.group(3)
    
    existing_items = len(re.findall(r'<div class="gallery-item', grid_content))
    print(f"Social Gallery has {existing_items} items")
    
    if existing_items < 6:
        new_items = ""
        for img in social_missing:
            new_items += f'\n                <div class="gallery-item reveal" style="background-image: url(\'images/{img}\');"></div>'
        
        grid_content = grid_content.rstrip() + new_items + "\n            "
        
        new_section = before_grid + grid_content + after_grid
        content = content[:match.start()] + new_section + content[match.end():]
        print(f"[OK] Added images to Social Gallery")

# Write optimized HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 80)
print("OPTIMIZATION COMPLETE")
print("=" * 80)
