from vex import *
import random
import math

mau = [Color.RED, Color.GREEN, Color.BLUE, Color.WHITE, Color.YELLOW, Color.ORANGE, Color.PURPLE]
brain = Brain()
screen = brain.screen

def screen_saver():
    while True:
        i = random.choice(mau)
        screen.set_pen_color(i)
        screen.set_fill_color(i)
        
        side_length = random.randint(2, 15)
        x = random.randint(0, 159)
        y = random.randint(0, 107)
        
        # Vẽ hình vuông xoay tròn đổi màu liên tục
        for angle in range(0, 360, 10):
            x_offset = side_length * math.cos(math.radians(angle))
            y_offset = side_length * math.sin(math.radians(angle))
            screen.draw_rectangle(x, y, side_length, side_length, angle)
            wait(20, MSEC)
            screen.draw_rectangle(x, y, side_length, side_length, angle, color=Color.BLACK)  # Xóa hình trước khi xoay

screen_saver()
