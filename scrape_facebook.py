#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrape Facebook photos from Aqua Terra page
"""
import os
import re
import sys
from scrapling.fetchers import StealthyFetcher

def scrape_facebook_photos():
    url = "https://www.facebook.com/aquaterralaketrichonida/photos_albums"
    
    print(f"[*] Scraping Facebook: {url}")
    print("[*] Lade Seite mit Cloudflare-Bypass...")
    
    try:
        # Seite laden mit Cloudflare-Solve
        page = StealthyFetcher.fetch(
            url,
            solve_cloudflare=True,
            wait=5000,  # 5 Sekunden warten für JS
            headless=True
        )
        
        print(f"[+] Seite geladen (Status: {page.status})")
        
        # Alle img-Tags finden
        images = page.css('img::attr(src)').getall()
        
        print(f"\n[*] Gefundene Bilder: {len(images)}")
        
        # Facebook-Bilder filtern (hdphotos, scontent)
        fb_images = []
        for img in images:
            if 'facebook.com' in img or 'fna.fbcdn.net' in img or 'scontent' in img:
                if img not in fb_images:  # Duplikate entfernen
                    fb_images.append(img)
        
        print(f"[+] Facebook-Bilder (ohne Dupes): {len(fb_images)}")
        
        # Ausgabe
        output_file = "facebook-images.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Facebook Photo URLs - Aqua Terra\n")
            f.write(f"# Source: {url}\n")
            f.write(f"# Count: {len(fb_images)}\n\n")
            for i, img_url in enumerate(fb_images, 1):
                f.write(f"{i}. {img_url}\n")
        
        print(f"\n[+] Gespeichert in: {output_file}")
        print("\n[*] Erste 10 Bilder:")
        for i, img in enumerate(fb_images[:10], 1):
            print(f"  {i}. {img[:100]}...")
            
        return fb_images
        
    except Exception as e:
        print(f"❌ Fehler: {e}")
        return []

if __name__ == "__main__":
    scrape_facebook_photos()
