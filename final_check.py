#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final check: Ensure ONLY new high-quality images are used
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")
images_dir = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/images")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all image references
all_images = re.findall(r"images/([^'\")\s]+\.jpg)", content)
unique_images = list(set(all_images))

print("=" * 80)
print("FINAL IMAGE CHECK - Aqua Terra Landing Page")
print("=" * 80)
print(f"\nTotal unique images used: {len(unique_images)}\n")

# Old images that should NOT be in the file
old_patterns = [
    'hero-exterior.jpg', 'interior-1.jpg', 'interior-2.jpg', 'food-1.jpg',
    'cocktail-1.jpg', 'terrace-1.jpg', 'atmosphere-1.jpg', 'detail-1.jpg',
    'detail-2.jpg', 'facebook-'
]

has_old = False
new_images_used = []

for img in sorted(unique_images):
    is_old = any(pattern in img for pattern in old_patterns)
    if is_old:
        print(f"[OLD] {img}")
        has_old = True
    else:
        size = "UNKNOWN"
        img_path = images_dir / img
        if img_path.exists():
            size = f"{img_path.stat().st_size/1024:.1f} KB"
        print(f"[NEW] {img:60s} ({size})")
        new_images_used.append(img)

print("\n" + "=" * 80)
if has_old:
    print("WARNING: Old images still present! Need replacement.")
else:
    print("SUCCESS: Only new high-quality images are used!")
print(f"Total new images: {len(new_images_used)}")
print("=" * 80)
