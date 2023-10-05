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
#    Project:           Iterating Though a 2D List
#    Description:       This example will show how to iterate through a
#                       2-dimensional list to access each member in the list
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Create a 2 dimensional list of values
my_list = [
    [2, 4, 6, 8, 10],
    [12, 14, 16, 18, 20],
    [22, 24, 26, 28, 30]
]

# Clear the robot's screen and set the cursor to the top left corner
brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

# Using a 'for loop', we can iterate through each row in the list
for row_count in range(3):
    # Using a second 'for loop',
    # we can iterate through each element in each row
    for element_count in range(5):
        # During each iteration,
        # the variable 'item' will be set to the value of
        # the specific element in the 2D list
        brain.screen.print(my_list[row_count][element_count])
        brain.screen.print(", ")
    brain.screen.next_row()
