#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze and select best images for Aqua Terra landing page
"""
import os
from pathlib import Path
from PIL import Image

def analyze_images():
    images_dir = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/images")
    
    print("=" * 80)
    print("AQUA TERRA IMAGE ANALYSIS")
    print("=" * 80)
    
    # Get all JPG files
    jpg_files = list(images_dir.glob("*.jpg"))
    print(f"\nTotal images found: {len(jpg_files)}\n")
    
    # Analyze each image
    image_data = []
    for img_path in jpg_files:
        try:
            with Image.open(img_path) as img:
                width, height = img.size
                size_kb = img_path.stat().st_size / 1024
                aspect_ratio = width / height
                
                # Determine category based on filename
                name_lower = img_path.name.lower()
                if 'hero' in name_lower or 'exterior' in name_lower:
                    category = 'EXTERIOR'
                elif 'interior' in name_lower or 'inside' in name_lower:
                    category = 'INTERIOR'
                elif 'food' in name_lower or 'dish' in name_lower or 'plate' in name_lower:
                    category = 'FOOD'
                elif 'cocktail' in name_lower or 'drink' in name_lower or 'bar' in name_lower:
                    category = 'COCKTAIL'
                elif 'terrace' in name_lower or 'view' in name_lower or 'lake' in name_lower:
                    category = 'TERRACE'
                elif 'atmosphere' in name_lower or 'detail' in name_lower:
                    category = 'ATMOSPHERE'
                else:
                    category = 'UNKNOWN'
                
                image_data.append({
                    'name': img_path.name,
                    'path': img_path,
                    'width': width,
                    'height': height,
                    'size_kb': size_kb,
                    'aspect_ratio': aspect_ratio,
                    'category': category,
                    'score': size_kb * 0.5 + (width * height) / 10000  # Simple quality score
                })
        except Exception as e:
            print(f"Error analyzing {img_path.name}: {e}")
    
    # Group by category
    categories = {}
    for img in image_data:
        cat = img['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(img)
    
    # Sort each category by score
    for cat in categories:
        categories[cat].sort(key=lambda x: x['score'], reverse=True)
    
    # Print recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDED IMAGES FOR LANDING PAGE")
    print("=" * 80)
    
    selections = {
        'HERO': None,
        'EXTERIOR': [],
        'INTERIOR': [],
        'FOOD': [],
        'COCKTAIL': [],
        'TERRACE': [],
        'ATMOSPHERE': []
    }
    
    # Select HERO (best exterior with landscape orientation)
    exterior_all = categories.get('EXTERIOR', []) + categories.get('TERRACE', [])
    exterior_all.sort(key=lambda x: x['score'], reverse=True)
    if exterior_all:
        selections['HERO'] = exterior_all[0]
        print(f"\n[HERO] HERO IMAGE:")
        print(f"   {selections['HERO']['name']}")
        print(f"   {selections['HERO']['width']}x{selections['HERO']['height']} | {selections['HERO']['size_kb']:.1f} KB")
    
    # Select top 2 additional EXTERIOR
    if len(exterior_all) > 1:
        selections['EXTERIOR'] = exterior_all[1:3]
        print(f"\n[EXTERIOR] EXTERIOR ({len(selections['EXTERIOR'])} images):")
        for img in selections['EXTERIOR']:
            print(f"   • {img['name']} ({img['width']}x{img['height']}, {img['size_kb']:.1f} KB)")
    
    # Select top 2 INTERIOR
    interior = categories.get('INTERIOR', [])
    if interior:
        selections['INTERIOR'] = interior[:2]
        print(f"\n[INTERIOR] INTERIOR ({len(selections['INTERIOR'])} images):")
        for img in selections['INTERIOR']:
            print(f"   • {img['name']} ({img['width']}x{img['height']}, {img['size_kb']:.1f} KB)")
    
    # Select top 3 FOOD
    food = categories.get('FOOD', [])
    if food:
        selections['FOOD'] = food[:3]
        print(f"\n[FOOD] FOOD ({len(selections['FOOD'])} images):")
        for img in selections['FOOD']:
            print(f"   • {img['name']} ({img['width']}x{img['height']}, {img['size_kb']:.1f} KB)")
    
    # Select top 2 COCKTAIL
    cocktail = categories.get('COCKTAIL', [])
    if cocktail:
        selections['COCKTAIL'] = cocktail[:2]
        print(f"\n[COCKTAIL] COCKTAIL ({len(selections['COCKTAIL'])} images):")
        for img in selections['COCKTAIL']:
            print(f"   • {img['name']} ({img['width']}x{img['height']}, {img['size_kb']:.1f} KB)")
    
    # Select top 2 TERRACE/VIEW
    terrace = categories.get('TERRACE', [])
    if terrace and selections['HERO'] not in terrace:
        selections['TERRACE'] = terrace[:2]
        print(f"\n[TERRACE] TERRACE ({len(selections['TERRACE'])} images):")
        for img in selections['TERRACE']:
            print(f"   • {img['name']} ({img['width']}x{img['height']}, {img['size_kb']:.1f} KB)")
    
    # Select top 2 ATMOSPHERE
    atmosphere = categories.get('ATMOSPHERE', [])
    if atmosphere:
        selections['ATMOSPHERE'] = atmosphere[:2]
        print(f"\n[ATMOSPHERE] ATMOSPHERE ({len(selections['ATMOSPHERE'])} images):")
        for img in selections['ATMOSPHERE']:
            print(f"   • {img['name']} ({img['width']}x{img['height']}, {img['size_kb']:.1f} KB)")
    
    # Summary
    print("\n" + "=" * 80)
    total_selected = 1 + sum(len(v) for v in selections.values() if isinstance(v, list))
    print(f"TOTAL SELECTED: {total_selected} images")
    print("=" * 80)
    
    return selections

if __name__ == "__main__":
    analyze_images()
