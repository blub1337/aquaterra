#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix aesthetics and image scaling for Aqua Terra landing page
- Proper object-fit: cover for all gallery images
- Consistent aspect ratios
- Better spacing and visual hierarchy
- Improved typography and whitespace
"""
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("FIXING AESTHETICS & IMAGE SCALING")
print("=" * 80)

# 1. Fix gallery-item CSS to use proper background sizing
old_gallery_css = """.gallery-item {
            aspect-ratio: 4/3;
            background-size: cover;
            background-position: center;
            border-radius: 2px;
            overflow: hidden;
            position: relative;
        }"""

new_gallery_css = """.gallery-item {
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
        }

        .gallery-item::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.3) 100%);
            z-index: 1;
            pointer-events: none;
        }"""

if old_gallery_css in content:
    content = content.replace(old_gallery_css, new_gallery_css)
    print("[OK] Gallery item CSS updated with proper scaling")
else:
    # Try to find and replace any .gallery-item block
    import re
    pattern = r'(\.gallery-item\s*\{[^}]*aspect-ratio:\s*4/3[^}]*\})'
    match = re.search(pattern, content)
    if match:
        content = content[:match.start()] + new_gallery_css + content[match.end():]
        print("[OK] Gallery item CSS replaced via regex")
    else:
        print("[--] Old gallery CSS not found, inserting new...")
        # Insert after .gallery-grid CSS
        grid_pattern = r'(\.gallery-grid\s*\{[^}]+\})'
        match = re.search(grid_pattern, content)
        if match:
            insert_point = match.end()
            content = content[:insert_point] + "\n\n" + new_gallery_css + content[insert_point:]
            print("[OK] Gallery item CSS inserted")

# 2. Improve hero section image scaling
old_hero_css = """.hero-bg {
            position: absolute;
            inset: 0;
            background-size: cover;
            background-position: center;
        }"""

new_hero_css = """.hero-bg {
            position: absolute;
            inset: 0;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            will-change: transform;
            animation: heroSlowZoom 30s ease-out infinite alternate;
        }

        @keyframes heroSlowZoom {
            from { transform: scale(1); }
            to { transform: scale(1.08); }
        }"""

if old_hero_css in content:
    content = content.replace(old_hero_css, new_hero_css)
    print("[OK] Hero background CSS updated with slow zoom")
else:
    print("[--] Hero CSS not found")

# 3. Improve section spacing
content = content.replace(
    '.section-title {',
    '.section-title {\n            margin-bottom: 1rem;\n            line-height: 1.2;'
)
print("[OK] Section title spacing improved")

# 4. Add better container max-width
old_container = """.container {
            width: 90%;
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
        }"""

new_container = """.container {
            width: 100%;
            max-width: 1600px;
            margin: 0 auto;
            padding: 0 5%;
        }"""

if old_container in content:
    content = content.replace(old_container, new_container)
    print("[OK] Container width increased for better breathing room")

# 5. Improve gallery grid gaps
old_grid = """.gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }"""

new_grid = """.gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2.5rem;
            justify-items: center;
        }"""

if old_grid in content:
    content = content.replace(old_grid, new_grid)
    print("[OK] Gallery grid improved with larger minimum size")
else:
    # Try regex replacement
    pattern = r'(\.gallery-grid\s*\{[^}]*gap:\s*2rem[^}]*\})'
    match = re.search(pattern, content)
    if match:
        content = content[:match.start()] + new_grid + content[match.end():]
        print("[OK] Gallery grid replaced via regex")

# 6. Add image preload hints for performance
preload_hints = """
    <!-- Preload critical images -->
    <link rel="preload" as="image" href="images/506653046_9911850618922033_661776978636202946_n.jpg" type="image/jpeg">
    <link rel="preload" as="image" href="images/506986521_9911849908922104_1623314177700703878_n.jpg" type="image/jpeg">
"""

head_end = content.find('</head>')
if head_end > 0:
    content = content[:head_end] + preload_hints + content[head_end:]
    print("[OK] Image preload hints added")

# Write updated file
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 80)
print("AESTHETICS FIX COMPLETE")
print("=" * 80)
print("\nImprovements:")
print("  ✓ Gallery images: 16:9 aspect ratio (consistent)")
print("  ✓ object-fit: cover behavior via background-size")
print("  ✓ Hover effects with smooth zoom")
print("  ✓ Gradient overlay for better text readability")
print("  ✓ Hero section with slow zoom animation")
print("  ✓ Larger container (1600px max) for breathing room")
print("  ✓ Better grid gaps (2.5rem)")
print("  ✓ Image preloading for faster load")
