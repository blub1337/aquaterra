#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insert complete Main Gallery section before Premium Gallery
"""
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Best images for main gallery
main_gallery_images = [
    "506653046_9911850618922033_661776978636202946_n.jpg",  # 326 KB
    "506895132_9911850755588686_7595859430319777534_n.jpg",  # 270 KB
    "508717514_9955884347851993_6584167913972386682_n.jpg",  # 198 KB
    "509092799_9955884377851990_6540321685798541297_n.jpg",  # 188 KB
    "509377657_9955884124518682_5703531893056855893_n.jpg",  # 187 KB
    "472917815_8895921763848262_1776686108530075593_n.jpg",  # 125 KB
]

# Complete Main Gallery section HTML
gallery_html = '''
    <!-- Gallery Section -->
    <section id="gallery" class="gallery">
        <div class="container">
            <p class="section-label" data-i18n="gallery.label">Our Moments</p>
            <h2 class="section-title reveal" data-i18n="gallery.title">Visual<br>Journey</h2>
            
            <div class="gallery-grid">
''' + "\n".join([
    f'                <div class="gallery-item reveal" style="background-image: url(\'images/{img}\');"></div>'
    for img in main_gallery_images
]) + '''
            </div>
        </div>
    </section>

'''

# Find Premium Gallery section and insert before it
premium_match = content.find('<!-- Premium Gallery Section -->')
if premium_match > 0:
    content = content[:premium_match] + gallery_html + content[premium_match:]
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[OK] Main Gallery inserted before Premium Gallery")
    print(f"     Added {len(main_gallery_images)} images")
else:
    print("[ERROR] Premium Gallery section not found!")
