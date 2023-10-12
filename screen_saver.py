from vex import *
import random

mau = [0 for x in range(7)]
brain=Brain()

def screen_saver():
    while True:
        mau = [Color.RED, Color.GREEN, Color.BLUE, Color.WHITE, Color.YELLOW, Color.ORANGE, Color.PURPLE]
        i = random.choice(mau)
        brain.screen.set_pen_color(i)
        brain.screen.set_fill_color(i)
        brain.screen.draw_rectangle(random.randint(0,159), random.randint(0,107), random.randint(2,15), random.randint(2,15))
        brain.screen.draw_circle(random.randint(0,159), random.randint(0,107), random.randint(2,15))
        wait(20, MSEC)

screen_saver()
