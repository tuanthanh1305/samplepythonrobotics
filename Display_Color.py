#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
touchled_2 = Touchled(Ports.PORT2)



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
#    Project:           Display Color
#    Description:       This example will show when the TouchLED is pressed,
#                       it will turn red, otherwise it will be green.
#    Brain Supported:   2nd generation
#    Configuration:     TouchLED on Port 2
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Use a while loop so the program keeps checking if the TouchLED is pressed
while True:
    if touchled_2.pressing():
        touchled_2.set_color(Color.RED)
    else:
        touchled_2.set_color(Color.GREEN)

    # A brief delay inside of a loop to allow other resources to run
    wait(20, MSEC)
