from panda_color import Color

if __name__ == "__main__":
    color = Color(255, 128, 64)
    
    print("=== GLSL-Style Swizzling Examples ===")
    print(f"Original color: {color}")
    
    # Single component access
    print(f"\nSingle component access:")
    print(f"color.r = {color.r}")
    print(f"color.g = {color.g}")
    print(f"color.b = {color.b}")

    # Multi-component access
    print(f"\nMulti-component access:")
    print(f"color.rgb = {color.rgb}")
    print(f"color.rg = {color.rg}")
    print(f"color.gb = {color.gb}")
    print(f"color.bgr = {color.bgr}")
    print(f"color.rrg = {color.rrg}")
    print(f"color.brb = {color.brb}")
    
    # Single component assignment
    print(f"\nSingle component assignment:")
    color.r = 200
    print(f"After color.r = 200: {color}")
    
    # Multi-component assignment
    print(f"\nMulti-component assignment:")
    color.rgb = (100, 150, 200)
    print(f"After color.rgb = (100, 150, 200): {color}")
    
    color.rg = (255, 0)
    print(f"After color.rg = (255, 0): {color}")
    
    # Swizzle assignment from another color's swizzle
    color2 = Color(50, 100, 150)
    print(f"\nSecond color: {color2}")
    
    color.rgb = color2.gbr  # Assign green, blue, red from color2
    print(f"After color.rgb = color2.gbr: {color}")
    
    color.rg = color2.bb  # Assign blue, blue from color2
    print(f"After color.rg = color2.bb: {color}")