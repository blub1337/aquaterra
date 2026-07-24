#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find all image references in index.html and identify old vs new images
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")
images_dir = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/images")

# Read HTML
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all image references
pattern = r"images/([^'\")\s]+\.jpg)"
matches = re.findall(pattern, content)

print("=" * 80)
print("CURRENTLY USED IMAGES IN index.html")
print("=" * 80)
print(f"\nTotal references found: {len(matches)}\n")

# List all available new images (large files)
new_images = [f.name for f in images_dir.glob("*.jpg") if f.stat().st_size > 100 * 1024]  # >100KB
old_images = ['hero-exterior.jpg', 'interior-1.jpg', 'interior-2.jpg', 'food-1.jpg', 
              'cocktail-1.jpg', 'terrace-1.jpg', 'atmosphere-1.jpg', 'detail-1.jpg', 
              'detail-2.jpg', 'facebook-exterior-1.jpg', 'facebook-food-1.jpg',
              'facebook-cocktail-1.jpg', 'facebook-interior-1.jpg', 'facebook-terrace-1.jpg',
              'facebook-atmosphere-1.jpg', 'facebook-food-2.jpg', 'facebook-exterior-2.jpg']

used_images = list(set(matches))  # Remove duplicates

print("Images currently used:")
for img in sorted(used_images):
    size = "UNKNOWN"
    img_path = images_dir / img
    if img_path.exists():
        size = f"{img_path.stat().st_size/1024:.1f} KB"
    
    status = "OLD" if img in old_images and not img.startswith('5') else "NEW"
    print(f"  {status} {img:60s} ({size})")

print("\n" + "=" * 80)
print("RECOMMENDATION: Replace old images with new large files")
print("=" * 80)

# Get top new images not yet used
all_new_large = [f.name for f in sorted(images_dir.glob("*.jpg"), key=lambda x: x.stat().st_size, reverse=True)[:20]]
not_used = [img for img in all_new_large if img not in used_images]

if not_used:
    print("\nTop new images NOT yet used:")
    for img in not_used[:10]:
        size = f"{images_dir.joinpath(img).stat().st_size/1024:.1f} KB"
        print(f"  [NEW] {img:60s} ({size})")
