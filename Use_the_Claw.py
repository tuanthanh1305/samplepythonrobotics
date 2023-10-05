#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
claw_motor = Motor(Ports.PORT4, False)



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
#    Project:           Use the Claw
#    Description:       This example will show how to open the claw to
#                       a specific position and hold that position.
#                       Next, slightly close the Claw to another position
#                       and hold that position.
#                       Finally, close the Claw to the original position.
#    Brain Supported:   2nd generation
#    Configuration:     Claw Motor in Port 4
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Take the current position of the Claw as zero
claw_motor.set_position(0, DEGREES)

# Set the Claw's timeout
claw_motor.set_timeout(2, SECONDS)

# Open up the Claw and hold the position for two seconds
claw_motor.spin_for(REVERSE, 60, DEGREES)
wait(2, SECONDS)

# Close the Claw slightly and hold that position for two seconds
claw_motor.spin_for(FORWARD, 25, DEGREES)
wait(2, SECONDS)

# Return the Claw to its original position
claw_motor.spin_to_position(0, DEGREES)
