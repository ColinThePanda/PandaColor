from panda_color import Colors

color = Colors.CORNFLOWER_BLUE

print(color.to_bytes(3, 'f32'))
print(color.to_bytes(4, 'f32'))
print(color.to_bytes(3, 'f64'))
print(color.to_bytes(4, 'f64'))
print(color.to_bytes(3, 'u8'))
print(color.to_bytes(4, 'u8'))