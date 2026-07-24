#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insert all gallery sections between Experience and Location
"""
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find insertion point (before Location Section)
location_marker = "<!-- Location Section -->"
insertion_point = content.find(location_marker)

if insertion_point < 0:
    print("[ERROR] Location Section not found!")
    exit(1)

print(f"[OK] Found Location Section at position {insertion_point}")

# Define all galleries HTML
galleries_html = """
    <!-- Gallery Section -->
    <section id="gallery" class="gallery">
        <div class="container">
            <p class="section-label" data-i18n="gallery.label">Our Moments</p>
            <h2 class="section-title reveal" data-i18n="gallery.title">Visual<br>Journey</h2>
            
            <div class="gallery-grid">
                <div class="gallery-item reveal" style="background-image: url('images/506986521_9911849908922104_1623314177700703878_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/505947241_9910989592341469_7562819216884758934_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/506895132_9911850755588686_7595859430319777534_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/505828493_9910989472341481_3879326001581608062_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/506338969_9911464522293976_9065926674286702476_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/506225610_9911464805627281_291665047100918668_n.jpg');"></div>
            </div>
        </div>
    </section>

    <!-- Premium Gallery Section -->
    <section id="premium-gallery" class="gallery" style="background: #0f0f0f;">
        <div class="container">
            <p class="section-label" data-i18n="premium.label">Exquisite Moments</p>
            <h2 class="section-title reveal" data-i18n="premium.title">Premium<br>Collection</h2>
            <p class="section-subtitle reveal" data-i18n="premium.subtitle">
                Handpicked high-resolution photography showcasing the essence of Aqua Terra
            </p>
            
            <div class="gallery-grid">
                <div class="gallery-item reveal" style="background-image: url('images/506092515_9911464528960642_855826723425992128_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/508717514_9955884347851993_6584167913972386682_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/509092799_9955884377851990_6540321685798541297_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/506531577_9910989595674802_731187341473502969_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/509377657_9955884124518682_5703531893056855893_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/510399090_9978560588917702_5067114327253013055_n.jpg');"></div>
            </div>
        </div>
    </section>

    <!-- Social Media Gallery Section -->
    <section id="social" class="gallery" style="background: var(--charcoal);">
        <div class="container">
            <p class="section-label" data-i18n="social.label">From Our Community</p>
            <h2 class="section-title reveal" data-i18n="social.title">Follow<br>@AquaTerra</h2>
            <p class="section-subtitle reveal" data-i18n="social.subtitle">
                Discover authentic moments captured by our guests at Lake Trichonida
            </p>
            
            <div class="gallery-grid">
                <div class="gallery-item reveal" style="background-image: url('images/512767505_10003671753073252_5148265983321598462_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/506596645_9910666155707146_5260446900210604315_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/506793449_9910666072373821_6984148882883502724_n.jpg');"></div>
                <div class="gallery-item reveal" style="background-image: url('images/506890874_9910666265707135_3569776020610174111_n.jpg');"></div>
            </div>
            
            <div class="reveal" style="text-align: center; margin-top: 3rem;">
                <a href="https://www.facebook.com/aquaterralaketrichonida" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="color: var(--gold); border-color: var(--gold);">
                    <span data-i18n="social.follow">Visit Our Facebook Page</span>
                </a>
            </div>
        </div>
    </section>

"""

# Insert galleries before Location Section
new_content = content[:insertion_point] + galleries_html + content[insertion_point:]

# Write updated file
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("[OK] All 3 gallery sections inserted successfully")
print("     - Main Gallery: 6 images")
print("     - Premium Gallery: 6 images")
print("     - Social Gallery: 4 images")
print("     Total: 16 gallery images")
