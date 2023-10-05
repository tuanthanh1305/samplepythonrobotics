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
#    Project:           Split Arcade
#    Description:       The Left up/down Controller Axis (A) will drive
#                       the robot forward and backwards.
#                       The Right left/right Controller Axis (C) will turn
#                       the robot left and right.
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

while True:
    # Get the positions of axis A and axis C
    axis_a_pos = controller.axisA.position()
    axis_c_pos = controller.axisC.position()

    if abs(axis_a_pos) + abs(axis_c_pos) > dead_band:
        left_motor.set_velocity((axis_a_pos + axis_c_pos), PERCENT)
        right_motor.set_velocity((axis_a_pos - axis_c_pos), PERCENT)
    else:
        left_motor.set_velocity(0, PERCENT)
        right_motor.set_velocity(0, PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)

    wait(20, MSEC)
