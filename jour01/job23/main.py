def draw_rectangle(width,height):
    width = "-"
    height ="|"
   

print(draw_rectangle(5,3))

# def draw_rectangle(self, x, y, w, h, color):
#         """Draw a rectangle.

#         Args:
#             x (int): Starting X position.
#             y (int): Starting Y position.
#             w (int): Width of rectangle.
#             h (int): Height of rectangle.
#             color (int): RGB565 color value.
#         """
#         x2 = x + w - 1
#         y2 = y + h - 1
#         self.draw_hline(x, y, w, color)
#         self.draw_hline(x, y2, w, color)
#         self.draw_vline(x, y, h, color)
#         self.draw_vline(x2, y, h, color) 