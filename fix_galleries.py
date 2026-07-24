#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix and optimize all gallery sections with best images
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the best images for each section
main_gallery_images = [
    "506653046_9911850618922033_661776978636202946_n.jpg",  # 326 KB - HERO (also in main gallery)
    "506895132_9911850755588686_7595859430319777534_n.jpg",  # 270 KB - Food/Interior
    "508717514_9955884347851993_6584167913972386682_n.jpg",  # 198 KB - Detail
    "509092799_9955884377851990_8540321685798541297_n.jpg",  # 188 KB - Cocktail
    "509377657_9955884124518682_5703531893056855893_n.jpg",  # 187 KB - Food
    "472917815_8895921763848262_1776686108530075593_n.jpg",  # 125 KB - Atmosphere
]

premium_gallery_images = [
    "505947241_9910989592341469_7562819216884758934_n.jpg",  # 286 KB - Terrace
    "505828493_9910989472341481_3879326001581608062_n.jpg",  # 253 KB - Food
    "506338969_9911464522293976_9065926674286702476_n.jpg",  # 242 KB - Food
    "506225610_9911464805627281_291665047100918668_n.jpg",   # 227 KB - Interior
    "506092515_9911464528960642_855826723425992128_n.jpg",   # 212 KB - Cocktail
    "506531577_9910989595674802_731187341473502969_n.jpg",   # 188 KB - Interior
]

social_gallery_images = [
    "510399090_9978560588917702_5067114327253013055_n.jpg",  # 99 KB
    "512767505_10003671753073252_5148265983321598462_n.jpg", # 83 KB
    "506596645_9910666155707146_5260446900210604315_n.jpg",  # 47 KB
    "506793449_9910666072373821_6984148882883502724_n.jpg",  # 47 KB
]

print("=" * 80)
print("FIXING GALLERY SECTIONS")
print("=" * 80)

# Helper to create gallery items
def create_gallery_items(images):
    return "\n".join([
        f'                <div class="gallery-item reveal" style="background-image: url(\'images/{img}\');"></div>'
        for img in images
    ])

# Fix Main Gallery (after Gallery Section title)
main_gallery_html = create_gallery_items(main_gallery_images)
main_pattern = r'(<section id="gallery-main".*?<div class="gallery-grid">)(.*?)(</div>\s*</section>)'
match = re.search(main_pattern, content, re.DOTALL)
if match:
    new_section = match.group(1) + "\n" + main_gallery_html + "\n            " + match.group(3)
    content = content[:match.start()] + new_section + content[match.end():]
    print(f"[OK] Main Gallery fixed with {len(main_gallery_images)} images")
else:
    print("[--] Main Gallery section not found")

# Fix Premium Gallery
premium_gallery_html = create_gallery_items(premium_gallery_images)
premium_pattern = r'(<section id="premium-gallery".*?<div class="gallery-grid">)(.*?)(</div>\s*</section>)'
match = re.search(premium_pattern, content, re.DOTALL)
if match:
    new_section = match.group(1) + "\n" + premium_gallery_html + "\n            " + match.group(3)
    content = content[:match.start()] + new_section + content[match.end():]
    print(f"[OK] Premium Gallery fixed with {len(premium_gallery_images)} images")
else:
    print("[--] Premium Gallery section not found")

# Fix Social Gallery
social_gallery_html = create_gallery_items(social_gallery_images)
social_pattern = r'(<section id="social".*?<div class="gallery-grid">)(.*?)(</div>\s*</section>)'
match = re.search(social_pattern, content, re.DOTALL)
if match:
    new_section = match.group(1) + "\n" + social_gallery_html + "\n            " + match.group(3)
    content = content[:match.start()] + new_section + content[match.end():]
    print(f"[OK] Social Gallery fixed with {len(social_gallery_images)} images")
else:
    print("[--] Social Gallery section not found")

# Write fixed HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 80)
print("GALLERIES FIXED SUCCESSFULLY")
print("=" * 80)
print(f"Total gallery images: {len(main_gallery_images) + len(premium_gallery_images) + len(social_gallery_images)}")
