from .color import Color

def lighten(color: Color, factor: float) -> Color:
    """Return a lightened version of the color (factor 0.0–1.0)."""
    factor = max(0.0, min(1.0, factor))
    new_r = min(255, int(color.r + (255 - color.r) * factor))
    new_g = min(255, int(color.g + (255 - color.g) * factor))
    new_b = min(255, int(color.b + (255 - color.b) * factor))
    return color.__class__(new_r, new_g, new_b)

def darken(color: Color, factor: float) -> Color:
    """Return a darkened version of the color (factor 0.0–1.0)."""
    factor = max(0.0, min(1.0, factor))
    new_r = int(color.r * (1.0 - factor))
    new_g = int(color.g * (1.0 - factor))
    new_b = int(color.b * (1.0 - factor))
    return color.__class__(new_r, new_g, new_b)

def invert(color: Color) -> Color:
    """Return inverted (complement) color."""
    return color.__class__(255 - color.r, 255 - color.g, 255 - color.b)

def grayscale(color: Color) -> Color:
    """Convert to grayscale using luminance formula (ITU-R BT.709)."""
    gray = int(0.2126 * color.r + 0.7152 * color.g + 0.0722 * color.b)
    return color.__class__(gray, gray, gray)

def blend(color1: Color, color2: Color, factor: float) -> Color:
    """Blend two colors together by factor (0.0–1.0)."""
    factor = max(0.0, min(1.0, factor))
    new_r = int(color1.r * (1 - factor) + color2.r * factor)
    new_g = int(color1.g * (1 - factor) + color2.g * factor)
    new_b = int(color1.b * (1 - factor) + color2.b * factor)
    return color1.__class__(new_r, new_g, new_b)

def clamp(color: Color) -> Color:
    r = max(0, min(255, color.r))
    g = max(0, min(255, color.g))
    b = max(0, min(255, color.b))
    return color.__class__(r, g, b)

def distance(c1: Color, c2: Color) -> float:
    """Euclidean distance between two colors in RGB space."""
    dr = c1.r - c2.r
    dg = c1.g - c2.g
    db = c1.b - c2.b
    return (dr**2 + dg**2 + db**2) ** 0.5