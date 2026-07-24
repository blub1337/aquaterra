#!/usr/bin/env python3
"""Generate premium favicon set for Aqua Terra restaurant."""

from PIL import Image, ImageDraw, ImageFont
import os
import json

# Configuration
OUTPUT_DIR = r"C:\Users\L33\.openclaw\workspace\projects\aqua-terra\favicon"
BG_COLOR = "#050505"  # Dark background
GOLD_COLOR = "#c9a962"  # Elegant gold
SOURCE_SIZE = 512

def create_source_image():
    """Create the 512x512 source image with elegant monogram."""
    img = Image.new('RGBA', (SOURCE_SIZE, SOURCE_SIZE), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Draw elegant circular border
    margin = 20
    draw.ellipse(
        [margin, margin, SOURCE_SIZE - margin, SOURCE_SIZE - margin],
        outline=GOLD_COLOR,
        width=3
    )
    
    # Draw inner decorative circle
    inner_margin = 35
    draw.ellipse(
        [inner_margin, inner_margin, SOURCE_SIZE - inner_margin, SOURCE_SIZE - inner_margin],
        outline=GOLD_COLOR,
        width=1
    )
    
    # Create elegant "AT" monogram for Aqua Terra
    # Using drawing primitives to create stylized letters
    
    # Letter "A" - left side
    a_center_x = SOURCE_SIZE // 2 - 50
    a_center_y = SOURCE_SIZE // 2
    
    # A frame
    draw.line([(a_center_x - 40, a_center_y + 50), (a_center_x, a_center_y - 60)], fill=GOLD_COLOR, width=8)
    draw.line([(a_center_x + 40, a_center_y + 50), (a_center_x, a_center_y - 60)], fill=GOLD_COLOR, width=8)
    draw.line([(a_center_x - 25, a_center_y + 10), (a_center_x + 25, a_center_y + 10)], fill=GOLD_COLOR, width=8)
    
    # Letter "T" - right side, connected elegantly
    t_center_x = SOURCE_SIZE // 2 + 50
    t_center_y = SOURCE_SIZE // 2
    
    # T top bar
    draw.line([(t_center_x - 45, t_center_y - 60), (t_center_x + 45, t_center_y - 60)], fill=GOLD_COLOR, width=8)
    # T vertical
    draw.line([(t_center_x, t_center_y - 60), (t_center_x, t_center_y + 50)], fill=GOLD_COLOR, width=8)
    
    # Add decorative elements - small dots at cardinal points
    dot_positions = [
        (SOURCE_SIZE // 2, 50),      # Top
        (SOURCE_SIZE // 2, SOURCE_SIZE - 50),  # Bottom
        (50, SOURCE_SIZE // 2),      # Left
        (SOURCE_SIZE - 50, SOURCE_SIZE // 2)   # Right
    ]
    
    for x, y in dot_positions:
        draw.ellipse([x-4, y-4, x+4, y+4], fill=GOLD_COLOR)
    
    # Add subtle wave element below monogram (representing "Aqua")
    wave_y = SOURCE_SIZE - 90
    wave_points = []
    for x in range(SOURCE_SIZE // 2 - 60, SOURCE_SIZE // 2 + 61, 10):
        offset = 5 if ((x - (SOURCE_SIZE // 2)) // 20) % 2 == 0 else -5
        wave_points.append((x, wave_y + offset))
    
    if len(wave_points) > 1:
        draw.line(wave_points, fill=GOLD_COLOR, width=3)
    
    return img

def resize_image(img, size):
    """Resize image using high-quality Lanczos resampling."""
    return img.resize(size, Image.Resampling.LANCZOS)

def create_favicon_ico(img):
    """Create multi-resolution .ico file."""
    sizes = [(16, 16), (32, 32), (48, 48)]
    ico_path = os.path.join(OUTPUT_DIR, "favicon.ico")
    
    # Convert to RGB for ICO (ICO doesn't support RGBA properly in all cases)
    img_rgb = img.convert('RGB')
    
    # Save as ICO with multiple resolutions
    img_rgb.save(ico_path, format='ICO', sizes=sizes)
    return ico_path

def save_png(img, size, filename):
    """Save as PNG at specified size."""
    resized = resize_image(img, size)
    filepath = os.path.join(OUTPUT_DIR, filename)
    resized.save(filepath, 'PNG')
    return filepath

def create_apple_touch_icon(img):
    """Create Apple Touch Icon (180x180)."""
    return save_png(img, (180, 180), "apple-touch-icon.png")

def create_android_icons(img):
    """Create Android Chrome icons."""
    files = []
    files.append(save_png(img, (192, 192), "android-chrome-192x192.png"))
    files.append(save_png(img, (512, 512), "android-chrome-512x512.png"))
    return files

def create_webmanifest():
    """Create site.webmanifest file."""
    manifest = {
        "name": "Aqua Terra",
        "short_name": "Aqua Terra",
        "description": "Premium Restaurant Experience",
        "icons": [
            {
                "src": "android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "theme_color": "#050505",
        "background_color": "#050505",
        "display": "standalone"
    }
    
    filepath = os.path.join(OUTPUT_DIR, "site.webmanifest")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    
    return filepath

def main():
    print("Generating premium favicon set for Aqua Terra restaurant...")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    # Create source image
    print("Creating 512x512 source image with elegant AT monogram...")
    source_img = create_source_image()
    source_path = os.path.join(OUTPUT_DIR, "favicon-512x512-source.png")
    source_img.save(source_path, 'PNG')
    print(f"  [OK] Created: {source_path}")
    
    # Generate all favicon formats
    created_files = []
    
    # Standard PNG favicons
    print("\nGenerating PNG favicons...")
    created_files.append(save_png(source_img, (32, 32), "favicon-32x32.png"))
    created_files.append(save_png(source_img, (16, 16), "favicon-16x16.png"))
    
    # ICO file (multi-resolution)
    print("Generating favicon.ico (16x16, 32x32, 48x48)...")
    created_files.append(create_favicon_ico(source_img))
    
    # Apple Touch Icon
    print("Generating apple-touch-icon.png (180x180)...")
    created_files.append(create_apple_touch_icon(source_img))
    
    # Android Chrome icons
    print("Generating Android Chrome icons...")
    created_files.extend(create_android_icons(source_img))
    
    # Web Manifest
    print("Generating site.webmanifest...")
    created_files.append(create_webmanifest())
    
    # Summary
    print("\n" + "="*60)
    print("FAVICON SET COMPLETE")
    print("="*60)
    print("\nCreated files:")
    for filepath in created_files:
        filename = os.path.basename(filepath)
        size = os.path.getsize(filepath)
        print(f"  [OK] {filename} ({size:,} bytes)")
    
    print(f"\nAll files saved to: {OUTPUT_DIR}")
    print("\nUsage in HTML:")
    print("""  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">""")

if __name__ == "__main__":
    main()
