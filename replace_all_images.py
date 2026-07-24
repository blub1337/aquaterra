#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Replace ALL old images with new high-quality images in index.html
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

# Read HTML
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Mapping: OLD filename -> NEW filename (best quality replacements)
replacements = {
    # Hero section - use absolute best
    '506653046_9911850618922033_661776978636202946_n.jpg': '506986521_9911849908922104_1623314177700703878_n.jpg',  # 304 KB instead of 326 KB
    
    # Interior - replace with large new files
    'interior-1.jpg': '506531577_9910989595674802_731187341473502969_n.jpg',  # Already using this (188 KB)
    '506531577_9910989595674802_731187341473502969_n.jpg': '506225610_9911464805627281_291665047100918668_n.jpg',  # 227 KB
    
    # Food - replace with best
    'food-1.jpg': '505828493_9910989472341481_3879326001581608062_n.jpg',  # 253 KB
    '505828493_9910989472341481_3879326001581608062_n.jpg': '506338969_9911464522293976_9065926674286702476_n.jpg',  # 242 KB
    '506338969_9911464522293976_9065926674286702476_n.jpg': '508717514_9955884347851993_6584167913972386682_n.jpg',  # 198 KB
    
    # Cocktail - replace
    'cocktail-1.jpg': '506092515_9911464528960642_855826723425992128_n.jpg',  # 212 KB (already using)
    '506092515_9911464528960642_855826723425992128_n.jpg': '509092799_9955884377851990_6540321685798541297_n.jpg',  # 188 KB
    
    # Terrace - replace
    'terrace-1.jpg': '505947241_9910989592341469_7562819216884758934_n.jpg',  # 286 KB (already using)
    '505947241_9910989592341469_7562819216884758934_n.jpg': '506895132_9911850755588686_7595859430319777534_n.jpg',  # 270 KB
    
    # Atmosphere/Details - replace small files
    'atmosphere-1.jpg': '509377657_9955884124518682_5703531893056855893_n.jpg',  # 187 KB
    'detail-1.jpg': '472917815_8895921763848262_1776686108530075593_n.jpg',  # 125 KB
    'detail-2.jpg': '510399090_9978560588917702_5067114327253013055_n.jpg',  # 99 KB
    
    # Facebook/Social - replace with larger versions
    'facebook-exterior-1.jpg': '506986521_9911849908922104_1623314177700703878_n.jpg',  # 304 KB
    'facebook-exterior-2.jpg': '509377657_9955884124518682_5703531893056855893_n.jpg',  # 187 KB
    'facebook-terrace-1.jpg': '472917815_8895921763848262_1776686108530075593_n.jpg',  # 125 KB
}

print("=" * 80)
print("REPLACING OLD IMAGES WITH NEW HIGH-QUALITY IMAGES")
print("=" * 80)

replacement_count = 0
for old_img, new_img in replacements.items():
    if old_img in content:
        content = content.replace(old_img, new_img)
        print(f"[OK] {old_img[:50]:50s} -> {new_img[:50]}")
        replacement_count += 1
    else:
        print(f"[--] {old_img[:50]:50s} (not found in HTML)")

# Write updated HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 80)
print(f"TOTAL REPLACEMENTS: {replacement_count}/{len(replacements)}")
print("=" * 80)
print("\n[OK] index.html updated successfully!")
