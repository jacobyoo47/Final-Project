import math
import arcade
import os

def displayTextBox(text, x, y, width, height, color):

    arcade.draw_rectangle_filled(x, y, width, height, color)
    
    arcade.draw_text(text, 20, height - 35, arcade.color.BLACK, 16)