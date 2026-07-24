#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete rebuild of gallery sections with ONLY new high-quality images
No old images, no broken references
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")
backup_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index-backup.html")

# Read backup (before we broke it)
with open(backup_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("COMPLETE GALLERY REBUILD - Using ONLY New High-Quality Images")
print("=" * 80)

# Define ALL best images (only large files, 100KB+)
best_images = {
    'hero': "506653046_9911850618922033_661776978636202946_n.jpg",  # 326 KB
    'main_gallery': [
        "506986521_9911849908922104_1623314177700703878_n.jpg",  # 304 KB
        "505947241_9910989592341469_7562819216884758934_n.jpg",  # 286 KB
        "506895132_9911850755588686_7595859430319777534_n.jpg",  # 270 KB
        "505828493_9910989472341481_3879326001581608062_n.jpg",  # 253 KB
        "506338969_9911464522293976_9065926674286702476_n.jpg",  # 242 KB
        "506225610_9911464805627281_291665047100918668_n.jpg",   # 227 KB
    ],
    'premium_gallery': [
        "506092515_9911464528960642_855826723425992128_n.jpg",   # 212 KB
        "508717514_9955884347851993_6584167913972386682_n.jpg",  # 198 KB
        "509092799_9955884377851990_6540321685798541297_n.jpg",  # 188 KB
        "506531577_9910989595674802_731187341473502969_n.jpg",   # 188 KB
        "509377657_9955884124518682_5703531893056855893_n.jpg",  # 187 KB
        "510399090_9978560588917702_5067114327253013055_n.jpg",  # 99 KB
    ],
    'social_gallery': [
        "512767505_10003671753073252_5148265983321598462_n.jpg", # 83 KB
        "506596645_9910666155707146_5260446900210604315_n.jpg",  # 47 KB
        "506793449_9910666072373821_6984148882883502724_n.jpg",  # 47 KB
        "506890874_9910666265707135_3569776020610174111_n.jpg",  # 46 KB
    ]
}

# Step 1: Replace HERO image
old_hero_patterns = [
    "hero-exterior.jpg",
    "506986521_9911849908922104_1623314177700703878_n.jpg",
]
for old in old_hero_patterns:
    if old in content:
        content = content.replace(old, best_images['hero'])
        print(f"[OK] HERO replaced: {old[:40]}... -> {best_images['hero'][:40]}...")

# Step 2: Replace ALL old gallery images with new ones
all_new_images = set(best_images['main_gallery'] + best_images['premium_gallery'] + best_images['social_gallery'])

# Remove all old gallery-item divs
content = re.sub(r'<div class="gallery-item reveal"[^>]*style="[^"]*images/[^"]*"[^>]*></div>', '', content)
print("[OK] Removed all old gallery items")

# Find and rebuild Main Gallery
main_items_html = "\n".join([
    f'                <div class="gallery-item reveal" style="background-image: url(\'images/{img}\');"></div>'
    for img in best_images['main_gallery']
])

main_pattern = r'(<section id="gallery" class="gallery">.*?<div class="gallery-grid">)(.*?)(</div>\s*</section>)'
match = re.search(main_pattern, content, re.DOTALL)
if match:
    new_section = f"{match.group(1)}\n{main_items_html}\n            {match.group(3)}"
    content = content[:match.start()] + new_section + content[match.end():]
    print(f"[OK] Main Gallery rebuilt with {len(best_images['main_gallery'])} images")
else:
    print("[--] Main Gallery not found")

# Find and rebuild Premium Gallery  
premium_items_html = "\n".join([
    f'                <div class="gallery-item reveal" style="background-image: url(\'images/{img}\');"></div>'
    for img in best_images['premium_gallery']
])

premium_pattern = r'(<section id="premium-gallery".*?<div class="gallery-grid">)(.*?)(</div>\s*</section>)'
match = re.search(premium_pattern, content, re.DOTALL)
if match:
    new_section = f"{match.group(1)}\n{premium_items_html}\n            {match.group(3)}"
    content = content[:match.start()] + new_section + content[match.end():]
    print(f"[OK] Premium Gallery rebuilt with {len(best_images['premium_gallery'])} images")
else:
    print("[--] Premium Gallery not found")

# Find and rebuild Social Gallery
social_items_html = "\n".join([
    f'                <div class="gallery-item reveal" style="background-image: url(\'images/{img}\');"></div>'
    for img in best_images['social_gallery']
])

social_pattern = r'(<section id="social".*?<div class="gallery-grid">)(.*?)(</div>\s*</section>)'
match = re.search(social_pattern, content, re.DOTALL)
if match:
    new_section = f"{match.group(1)}\n{social_items_html}\n            {match.group(3)}"
    content = content[:match.start()] + new_section + content[match.end():]
    print(f"[OK] Social Gallery rebuilt with {len(best_images['social_gallery'])} images")
else:
    print("[--] Social Gallery not found")

# Write final HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

total = len(best_images['main_gallery']) + len(best_images['premium_gallery']) + len(best_images['social_gallery'])
print("\n" + "=" * 80)
print(f"REBUILD COMPLETE - Total gallery images: {total}")
print("=" * 80)
