#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add more high-quality images to the landing page galleries
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")
images_dir = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/images")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Get top 20 largest images
all_images = sorted(
    [(f.name, f.stat().st_size/1024) for f in images_dir.glob("*.jpg") if f.name.startswith('5') or f.name.startswith('4')],
    key=lambda x: x[1],
    reverse=True
)[:20]

print("=" * 80)
print("TOP 20 LARGEST IMAGES TO ADD")
print("=" * 80)
for i, (name, size) in enumerate(all_images, 1):
    print(f"{i:2d}. {name:60s} {size:8.1f} KB")

# Currently used images
used_pattern = r"images/([^'\")\s]+\.jpg)"
currently_used = set(re.findall(used_pattern, content))

print(f"\nCurrently used: {len(currently_used)} images")
print(f"Available to add: {len(all_images) - len(currently_used)} images")

# Find gallery sections and expand them
gallery_sections = []
for match in re.finditer(r'(<div class="gallery-grid">)(.*?)(</div>)', content, re.DOTALL):
    gallery_sections.append({
        'start': match.start(),
        'end': match.end(),
        'content': match.group(2)
    })

print(f"\nFound {len(gallery_sections)} gallery sections")

# Count existing gallery items
existing_items = len(re.findall(r'<div class="gallery-item reveal"', content))
print(f"Existing gallery items: {existing_items}")

# We want at least 12-16 gallery items total
target_items = 16
items_to_add = target_items - existing_items

if items_to_add > 0:
    print(f"\nNeed to add {items_to_add} more gallery items")
    
    # Find unused large images
    unused_large = [img for img, size in all_images if img not in currently_used][:items_to_add]
    
    print("\nImages to add:")
    for img in unused_large:
        print(f"  + {img}")
else:
    print("\n[OK] Sufficient gallery items already present")
