#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
arm_motor = Motor(Ports.PORT10, True)



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
#    Project:           Use the Arm
#    Description:       This example will show all how to lift the Arm to a
#                       specific position and hold that position.
#                       Next, lower the arm and hold that position.
#                       Stop the motor at the end of the program
#                       so that the Arm returns to its original position.
#    Brain Supported:   2nd generation
#    Configuration:     Arm Motor in Port 10
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Take the current postion of the Arm as zero
arm_motor.set_position(0, DEGREES)

# Move the Arm up and hold the position for 2 seconds
arm_motor.spin_for(FORWARD, 90, DEGREES)
wait(2, SECONDS)

# Lower the Arm and hold that position for 2 seconds
arm_motor.spin_for(REVERSE, 20, DEGREES)
wait(2, SECONDS)

# Stop the motor. The arm will now lower all the way down due to gravity
arm_motor.stop()
