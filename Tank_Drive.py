#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_motor = Motor(Ports.PORT1, False)
right_motor = Motor(Ports.PORT6, True)
controller = Controller()



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
#    Project:           Tank Drive
#    Description:       The Left up/down Controller Axis (A) will control the
#                       speed of the left motor.
#                       The Right up/down Controller Axis (D) will control the
#                       speed of the right motor.
#                       The deadband variable prevents drift when
#                       the Controller's joystick is released.
#    Brain Supported:   2nd generation
#    Configuration:     Left Motor in Port 1
#                       Right Motor in Port 6
#                       Controller
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Set the deadband variable
dead_band = 5

# Main controller loop to set motor velocities to controller axis positions
while True:
    if abs(controller.axisA.position()) > dead_band:
        left_motor.set_velocity(controller.axisA.position(), PERCENT)
    else:
        left_motor.set_velocity(0, PERCENT)
    if abs(controller.axisD.position()) > dead_band:
        right_motor.set_velocity(controller.axisD.position(), PERCENT)
    else:
        right_motor.set_velocity(0, PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)

    wait(20, MSEC)
