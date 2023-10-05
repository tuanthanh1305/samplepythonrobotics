#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
pneumatic_5 = Pneumatic(Ports.PORT5)



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
#    Project:           IQ Pneumatics
#    Description:       This example will switch between having pneumatics
#                       cylinder 1 and cylinder 2 extended. When neither
#                       cylinder is extended, the air pump will turn off.
#    Brain Supported:   2nd generation
#    Configuration:     Pneumatics in Port 5
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

while True:
    # Turn on the air pump so the cylinders will move
    pneumatic_5.pump_on()
    # Extend cylinder 1 for 2 seconds
    pneumatic_5.extend(CYLINDER1)
    wait(2, SECONDS)
    pneumatic_5.retract(CYLINDER1)
    # Extend cylinder 2 for 2 seconds
    pneumatic_5.extend(CYLINDER2)
    wait(2, SECONDS)
    pneumatic_5.retract(CYLINDER2)
    # Turn off the air pump after a short delay since we are not moving the cylinders
    wait(1, SECONDS)
    pneumatic_5.pump_off()
    # Wait 10 seconds before repeating the cycle
    wait(10, SECONDS)
