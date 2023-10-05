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
#    Project:           Creating Classes
#    Description:       This example will show how to create classes in VEXcode
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *


# Begin project code
# Create a class by using the "class" keyword
class TrackValues:
    # When creating a instance of a class, the "init" function will run
    # automatically. the "self" keyword refers the function to use values and
    # variable within the instance of the class
    def __init__(self, value):
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        self.value = value

    # Class functions can use standard robot commands
    def print_value(self):
        brain.screen.print("Current Value:", self.value)
        brain.screen.next_row()

    # Class functions can accept parameters
    def reset_value(self, new_value):
        self.value = new_value

    # Class functions can return values
    def get_value(self):
        return (self.value)

    # Class functions can modify variables
    def add_one(self):
        self.value += 1

    def sub_one(self):
        self.value -= 1

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO15)

# An instance (a copy) of a class can be created by using the constructor
# and passing the required parameters.
instance_1 = TrackValues(36)

# Functions within the class can be called using the format
# "instance name"."function name"("parameters")
instance_1.print_value()

# Class instance functions can be used multiple times
instance_1.add_one()
instance_1.print_value()

instance_1.sub_one()
instance_1.print_value()

# Class instance functions can accept parameters
instance_1.reset_value(50)
instance_1.print_value()
