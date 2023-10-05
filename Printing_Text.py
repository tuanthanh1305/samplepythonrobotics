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
#    Project:           Printing Text
#    Description:       This example will show how to print text to the
#                       robot's screen
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Erase the screen at the beginning of the project and
# set the printing location (cursor) to the top left corner
brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO15)

# Print and move the cursor down to the next line
brain.screen.print("Hello")
brain.screen.next_row()
wait(1, SECONDS)
brain.screen.print("Welcome!")

# Move the cursor down to the next line
brain.screen.next_row()
wait(1, SECONDS)
brain.screen.print("Goodbye!")

# The text will be cleared in 3 seconds
wait(3, SECONDS)
brain.screen.clear_screen()
