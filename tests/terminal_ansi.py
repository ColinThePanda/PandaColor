from panda_color import Color, color_text, highlight_text

if __name__ == "__main__":
    color = Color(99, 149, 238) # Cornflower Blue
    print(color_text("This text is in the color defined by the Color object!", color))
    print(highlight_text("This text is in the background color defined by the Color object!\n", color))

    color = Color(220, 20, 60) # Crimson
    print(color_text("This text is in the color defined by the Color object!", color))
    print(highlight_text("This text is in the background color defined by the Color object!\n", color))

    color = Color(50, 205, 50) # Lime Green
    print(color_text("This text is in the color defined by the Color object!", color))
    print(highlight_text("This text is in the background color defined by the Color object!\n", color))

    color = Color(255, 215, 0) # Gold
    print(color_text("This text is in the color defined by the Color object!", color))
    print(highlight_text("This text is in the background color defined by the Color object!\n", color))

    color = Color.random()
    print(color_text("This text is in the color defined by the Color object!", color))
    print(highlight_text("This text is in the background color defined by the Color object!\n", color))