#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete aesthetic redesign with proper image scaling
- Use <img> tags with object-fit instead of background-image
- Professional spacing and typography
- Better visual hierarchy
- Smooth animations
"""
from pathlib import Path
import re

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("COMPLETE REDESIGN - PROPER IMAGE SCALING")
print("=" * 80)

# Replace ALL gallery-item divs with background-image to proper img tags
def convert_gallery_item(match):
    bg_match = re.search(r"background-image:\s*url\(['\"]?images/([^'\")]+)['\"]?\)", match.group(1))
    if bg_match:
        img_name = bg_match.group(1)
        return f'<div class="gallery-item reveal"><img src="images/{img_name}" alt="Aqua Terra Gallery Image" loading="lazy"></div>'
    return match.group(0)

# Convert all gallery items
content = re.sub(r'<div class="gallery-item reveal"[^>]*style="([^"]*)"[^>]*></div>', convert_gallery_item, content)
print("[OK] Converted all gallery-items from background-image to <img> tags")

# Now update CSS for proper img scaling inside gallery-items
old_gallery_item_css = """.gallery-item {
            aspect-ratio: 16/9;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 4px;
            overflow: hidden;
            position: relative;
            transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1), filter 0.6s ease;
            filter: brightness(0.95);
        }

        .gallery-item:hover {
            transform: scale(1.03);
            filter: brightness(1.05);
            z-index: 10;
        }"""

new_gallery_item_css = """.gallery-item {
            position: relative;
            aspect-ratio: 4/3;
            border-radius: 2px;
            overflow: hidden;
            background: #1a1a1a;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }

        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            transition: transform 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            display: block;
        }

        .gallery-item:hover img {
            transform: scale(1.1);
        }

        .gallery-item::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.4) 100%);
            pointer-events: none;
            opacity: 0.6;
        }"""

if old_gallery_item_css in content:
    content = content.replace(old_gallery_item_css, new_gallery_item_css)
    print("[OK] Updated gallery-item CSS for <img> tags with object-fit: cover")
else:
    print("[--] Looking for gallery CSS to replace...")
    # Find and replace any .gallery-item block
    pattern = r'(\.gallery-item\s*\{[^}]*aspect-ratio:[^}]*\}(?:\s*\n\s*\.gallery-item:hover\s*\{[^}]*\})?)'
    match = re.search(pattern, content)
    if match:
        content = content[:match.start()] + new_gallery_item_css + content[match.end():]
        print("[OK] Replaced gallery CSS via regex")

# Improve hero section with proper image
old_hero_structure = """<div class="hero-bg" style="background-image: url('images/506653046_9911850618922033_661776978636202946_n.jpg');"></div>"""
new_hero_structure = """<picture class="hero-bg">
                <img src="images/506653046_9911850618922033_661776978636202946_n.jpg" alt="Aqua Terra Restaurant Lake Trichonida" style="width:100%;height:100%;object-fit:cover;object-position:center;">
            </picture>"""

if old_hero_structure in content:
    content = content.replace(old_hero_structure, new_hero_structure)
    print("[OK] Updated hero to use <img> tag")

# Update hero CSS
old_hero_css = """.hero-bg {
            position: absolute;
            inset: 0;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            will-change: transform;
            animation: heroSlowZoom 30s ease-out infinite alternate;
        }"""

new_hero_css = """.hero-bg {
            position: absolute;
            inset: 0;
            overflow: hidden;
        }

        .hero-bg img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            animation: heroSlowZoom 30s ease-out infinite alternate;
        }"""

if old_hero_css in content:
    content = content.replace(old_hero_css, new_hero_css)
    print("[OK] Updated hero CSS for <img> tag")

# Write updated file
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 80)
print("REDESIGN COMPLETE")
print("=" * 80)
print("\nKey improvements:")
print("  - All galleries now use <img> tags (not background-image)")
print("  - object-fit: cover ensures perfect scaling")
print("  - 4:3 aspect ratio for consistent grid")
print("  - Smooth hover zoom (1.1x scale)")
print("  - Gradient overlay for depth")
print("  - Box shadows for card elevation")
print("  - Hero section uses <img> with object-fit")
