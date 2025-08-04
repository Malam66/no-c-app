from PIL import Image, ImageDraw, ImageFont
import os

def create_nice_icon():
    # Create a 256x256 icon (standard size for Windows)
    size = 256
    icon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(icon)
    
    # Create a modern gradient background
    for y in range(size):
        for x in range(size):
            # Create a blue to purple gradient
            r = int(30 + (x / size) * 50)
            g = int(50 + (y / size) * 80)
            b = int(150 + ((x + y) / (2 * size)) * 100)
            icon.putpixel((x, y), (r, g, b, 255))
    
    # Draw a shield-like shape (representing protection/anti-recoil)
    shield_points = [
        (size//2, size//8),  # Top point
        (size//4, size//3),  # Left curve
        (size//4, size*2//3), # Left bottom
        (size//2, size*7//8), # Bottom point
        (size*3//4, size*2//3), # Right bottom
        (size*3//4, size//3),  # Right curve
    ]
    
    # Draw shield with white border
    draw.polygon(shield_points, fill=(255, 255, 255, 200), outline=(255, 255, 255, 255), width=3)
    
    # Draw inner shield with blue fill
    inner_shield_points = [
        (size//2, size//6),
        (size//3, size//3),
        (size//3, size*2//3),
        (size//2, size*5//6),
        (size*2//3, size*2//3),
        (size*2//3, size//3),
    ]
    draw.polygon(inner_shield_points, fill=(70, 130, 180, 200))
    
    # Draw a crosshair in the center
    center = size // 2
    crosshair_size = size // 8
    
    # Vertical line
    draw.line([(center, center - crosshair_size), (center, center + crosshair_size)], 
              fill=(255, 255, 255, 255), width=4)
    # Horizontal line
    draw.line([(center - crosshair_size, center), (center + crosshair_size, center)], 
              fill=(255, 255, 255, 255), width=4)
    
    # Draw small circles at the ends
    circle_radius = 6
    for x, y in [(center, center - crosshair_size), (center, center + crosshair_size),
                  (center - crosshair_size, center), (center + crosshair_size, center)]:
        draw.ellipse([x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius], 
                    fill=(255, 255, 255, 255))
    
    # Save as ICO file
    icon.save('app_icon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    
    # Also save as PNG for preview
    icon.save('app_icon.png', format='PNG')
    
    print("✅ Nice icon created: app_icon.ico")
    print("📁 Icon saved as: app_icon.ico (for installer)")
    print("📁 Preview saved as: app_icon.png")
    
    return 'app_icon.ico'

if __name__ == "__main__":
    try:
        create_nice_icon()
    except ImportError:
        print("❌ PIL/Pillow not installed. Installing...")
        import subprocess
        subprocess.run(["pip", "install", "Pillow"])
        create_nice_icon() 