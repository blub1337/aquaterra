#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update landing page with best images from the images folder
Selects largest/highest quality images for each category
"""
import os
import re
from pathlib import Path

images_dir = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/images")
html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

# Get all JPG files sorted by size (largest first)
all_images = sorted(
    [f for f in images_dir.glob("*.jpg")],
    key=lambda x: x.stat().st_size,
    reverse=True
)

print(f"Total images: {len(all_images)}")
print("\nTop 20 largest images:")
for i, img in enumerate(all_images[:20], 1):
    print(f"{i:2d}. {img.name:60s} {img.stat().st_size/1024:8.1f} KB")

# Select best images for each slot (avoiding Google Maps view images)
# Based on filename patterns and size

# HERO: Best exterior/landscape shot
hero_candidates = [f for f in all_images if any(x in f.name.lower() for x in ['hero', 'exterior', 'terrace', '506986521', '506653046'])]
hero = hero_candidates[0] if hero_candidates else all_images[0]

# INTERIOR: Best interior shots
interior_candidates = [f for f in all_images if 'interior' in f.name.lower() or '506531577' in f.name]
interior_1 = interior_candidates[0] if len(interior_candidates) > 0 else all_images[5]
interior_2 = interior_candidates[1] if len(interior_candidates) > 1 else all_images[10]

# FOOD: Best food shots
food_candidates = [f for f in all_images if 'food' in f.name.lower() or '505828493' in f.name or '506338969' in f.name or '509377657' in f.name]
food_1 = food_candidates[0] if food_candidates else all_images[7]
food_2 = food_candidates[1] if len(food_candidates) > 1 else all_images[8]
food_3 = food_candidates[2] if len(food_candidates) > 2 else all_images[12]

# COCKTAIL: Best cocktail/bar shots
cocktail_candidates = [f for f in all_images if 'cocktail' in f.name.lower() or '506092515' in f.name]
cocktail_1 = cocktail_candidates[0] if cocktail_candidates else all_images[8]
cocktail_2 = cocktail_candidates[1] if len(cocktail_candidates) > 1 else all_images[12]

# TERRACE/VIEW: Best terrace/lake views
terrace_candidates = [f for f in all_images if 'terrace' in f.name.lower() or '506895132' in f.name or '505947241' in f.name]
terrace_1 = terrace_candidates[0] if terrace_candidates else all_images[3]
terrace_2 = terrace_candidates[1] if len(terrace_candidates) > 1 else all_images[6]

# ATMOSPHERE/DETAILS
detail_candidates = [f for f in all_images if 'detail' in f.name.lower() or 'atmosphere' in f.name.lower() or '506596645' in f.name]
detail_1 = detail_candidates[0] if detail_candidates else all_images[20]
detail_2 = detail_candidates[1] if len(detail_candidates) > 1 else all_images[22]

# SOCIAL (Facebook images)
social_candidates = [f for f in all_images if 'facebook' in f.name.lower()]
social_1 = social_candidates[0] if len(social_candidates) > 0 else all_images[-1]
social_2 = social_candidates[1] if len(social_candidates) > 1 else all_images[-2]
social_3 = social_candidates[2] if len(social_candidates) > 2 else all_images[-3]
social_4 = social_candidates[3] if len(social_candidates) > 3 else all_images[-4]

print("\n" + "="*80)
print("SELECTED IMAGES FOR LANDING PAGE")
print("="*80)
print(f"\nHERO:          {hero.name}")
print(f"INTERIOR 1:    {interior_1.name}")
print(f"INTERIOR 2:    {interior_2.name}")
print(f"FOOD 1:        {food_1.name}")
print(f"FOOD 2:        {food_2.name}")
print(f"FOOD 3:        {food_3.name}")
print(f"COCKTAIL 1:    {cocktail_1.name}")
print(f"COCKTAIL 2:    {cocktail_2.name}")
print(f"TERRACE 1:     {terrace_1.name}")
print(f"TERRACE 2:     {terrace_2.name}")
print(f"DETAIL 1:      {detail_1.name}")
print(f"DETAIL 2:      {detail_2.name}")
print(f"SOCIAL 1:      {social_1.name}")
print(f"SOCIAL 2:      {social_2.name}")
print(f"SOCIAL 3:      {social_3.name}")
print(f"SOCIAL 4:      {social_4.name}")

# Save selections to file for manual update
selections = {
    'hero': hero.name,
    'interior_1': interior_1.name,
    'interior_2': interior_2.name,
    'food_1': food_1.name,
    'food_2': food_2.name,
    'food_3': food_3.name,
    'cocktail_1': cocktail_1.name,
    'cocktail_2': cocktail_2.name,
    'terrace_1': terrace_1.name,
    'terrace_2': terrace_2.name,
    'detail_1': detail_1.name,
    'detail_2': detail_2.name,
    'social_1': social_1.name,
    'social_2': social_2.name,
    'social_3': social_3.name,
    'social_4': social_4.name,
}

# Write selections to JSON-like file
with open(images_dir.parent / 'selected_images.txt', 'w', encoding='utf-8') as f:
    f.write("# Selected Images for Aqua Terra Landing Page\n")
    f.write("# Generated automatically based on file size and quality\n\n")
    for key, value in selections.items():
        f.write(f"{key} = {value}\n")

print(f"\n[OK] Selections saved to: selected_images.txt")
print("\nNext step: Manually update index.html with these image filenames")
