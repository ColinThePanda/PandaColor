from panda_color import RGB

if __name__ == "__main__":
    color = RGB(99, 149, 238) # Cornflower Blue
    print(color.color_text_foreground("This text is in the color defined by the RGB object!"))
    print(color.color_text_background("This text is in the background color defined by the RGB object!"))
    print()

    color = RGB(220, 20, 60) # Crimson
    print(color.color_text_foreground("This text is in the color defined by the RGB object!"))
    print(color.color_text_background("This text is in the background color defined by the RGB object!"))
    print()

    color = RGB(50, 205, 50) # Lime Green
    print(color.color_text_foreground("This text is in the color defined by the RGB object!"))
    print(color.color_text_background("This text is in the background color defined by the RGB object!"))
    print()

    color = RGB(255, 215, 0) # Gold
    print(color.color_text_foreground("This text is in the color defined by the RGB object!"))
    print(color.color_text_background("This text is in the background color defined by the RGB object!"))
    print()

    color = RGB.random()
    print(color.color_text_foreground("This text is in the color defined by the RGB object!"))
    print(color.color_text_background("This text is in the background color defined by the RGB object!"))
    print()