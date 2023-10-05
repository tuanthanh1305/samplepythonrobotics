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
#    Project:           Passing Parameters
#    Description:       This example will show how to create and use
#                       functions with parameters within your project
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *


# Functions are created by using the 'def' keyword along with
# the name of the function, any parameters will be defined in the parenthesis
# finally a colon to denote the beginning of the function.
def my_function_1(parameter1):
    brain.screen.next_row()
    brain.screen.print("Function 1:", parameter1)


# Multiple functions can be defined within the same project
# Multiple parameters are separated by a comma
def my_function_2(parameter1, parameter2):
    brain.screen.next_row()
    brain.screen.print("Function 2:", parameter1)
    brain.screen.print(",", parameter2)

# Begin project code
brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

brain.screen.print("Start of Function Calls")

# Functions are "called" by using the name of the function like a command
# and passing the values of each parameters within the parenthesis
my_function_1(50)
my_function_2(100, 200)
my_function_1(300)

brain.screen.next_row()
brain.screen.print("End of Function Calls")
