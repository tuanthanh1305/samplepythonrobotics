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
#    Project:           Printing Values
#    Description:       This example will print the timer's value to the
#                       robot's screen
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

while True:
    # Each iteration of the loop will clear the screen
    brain.screen.clear_screen()

    # After clearing the screen, set the printing cursor back to the top left
    # corner
    brain.screen.set_cursor(1, 1)

    # Print a label and the value of the timer on the same line
    brain.screen.print(
        "Timer (Seconds):", brain.timer.time(SECONDS), precision=2)
    wait(20, MSEC)
