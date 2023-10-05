#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()



# Make random actually random
def setRandomSeedUsingAccel():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    urandom.seed(int(xaxis + yaxis + zaxis))
    
# Set random seed 
setRandomSeedUsingAccel()

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------------------------------------------
#
#    Project:           Printing Lines and Shapes
#    Description:       This example will show how to use different drawing
#                       commands to draw shapes and lines on the Brain's screen
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Pen Color sets the color for text, lines, and outlines of shapes
brain.screen.set_pen_color(Color.RED)

# Fill Color sets the color for the inside fill of shapes
brain.screen.set_fill_color(Color.BLUE)

# Pen Width is used to set the thickness of lines and outlines of shapes
brain.screen.set_pen_width(2)

# Individual pixels will be drawn with the current pen color
brain.screen.draw_pixel(5, 5)

# Lines can be drawn by setting the beginning and end pixel coordinates
brain.screen.draw_line(60, 25, 75, 40)

# Rectangles are drawn by setting the top left corner of the rectangle
# then setting the height and width of the rectangle
brain.screen.draw_rectangle(85, 25, 15, 15)

# Circles are drawn by setting the center X/Y coordinate of the circle
# then setting the radius of the circle
brain.screen.draw_circle(80, 65, 15)
