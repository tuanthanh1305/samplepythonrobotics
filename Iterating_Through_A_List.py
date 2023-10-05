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
#    Project:           Iterating Through A List
#    Description:       This example will show how to iterate through a
#                       list to access each member in the list of values
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Create a list of values, with commas separating each value
my_list = [2, 4, 6, 8, 10]

# Clear the robot's screen and set the cursor to the top left corner
brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)

# Using a 'for loop', we can iterate through each element in the list
for item in range(5):
    # During each iteration, the variable 'item' will be set to the value of
    # the specific element in the list
    brain.screen.print(my_list[item])
    brain.screen.print(",")

brain.screen.next_row()
brain.screen.print("Completed!")
