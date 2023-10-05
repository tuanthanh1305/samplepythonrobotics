#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_motor = Motor(Ports.PORT1, False)
right_motor = Motor(Ports.PORT6, True)
claw_motor = Motor(Ports.PORT4, False)
arm_motor = Motor(Ports.PORT10, True)
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
#    Project:           Clawbot Controller with Events
#    Description:       The Left up/down Controller Axis (A) will control the
#                       speed of the left motor.
#                       The Right up/down Controller Axis (D) will control the
#                       speed of the right motor.
#                       The Left up/down Controller Buttons will control
#                       the Arm
#                       The Right up/down Controller Buttons will control
#                       the Claw
#    Brain Supported:   2nd generation
#    Configuration:     Controller
#                       Left Motor in Port 1
#                       Right Motor in Port 6
#                       Claw Motor in Port 4
#                       Arm Motor in Port 10
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *


# Begin project code
# Callback function when Controller buttonLUp is pressed
def on_L_up_pressed():
    # Spinning the arm_motor in forward raises the Arm
    arm_motor.spin(FORWARD)

    while controller.buttonLUp.pressing():
        # Wait until buttonLup is released
        wait(20, MSEC)

    arm_motor.stop()


# Callback function when Controller buttonLDown is pressed
def on_L_down_pressed():
    # Spinning the arm_motor in reverse lowers the Arm
    arm_motor.spin(REVERSE)

    while controller.buttonLDown.pressing():
        # Wait until buttonLDown is released
        wait(20, MSEC)

    arm_motor.stop()


# Callback function when Controller buttonRUp is pressed
def on_R_up_pressed():
    # Spinning the claw_motor forward closes the Claw
    claw_motor.spin(FORWARD)

    while controller.buttonRUp.pressing():
        # Wait until buttonRUp is released
        wait(20, MSEC)

    claw_motor.stop()


# Callback function when Controller buttonRDown is pressed
def on_R_down_pressed():
    # Spinning the claw_motor in reverse opens the Claw
    claw_motor.spin(REVERSE)

    while controller.buttonRDown.pressing():
        # Wait until buttonRDown is released
        wait(20, MSEC)

    claw_motor.stop()


# Register event handlers and pass callback functions
controller.buttonLUp.pressed(on_L_up_pressed)
controller.buttonLDown.pressed(on_L_down_pressed)
controller.buttonRUp.pressed(on_R_up_pressed)
controller.buttonRDown.pressed(on_R_down_pressed)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

# Set default motor stopping behavior and velocity
arm_motor.set_stopping(HOLD)
claw_motor.set_stopping(HOLD)
arm_motor.set_velocity(60, PERCENT)
claw_motor.set_velocity(30, PERCENT)

# Loop to check Controller Axis positions and set motor velocity
while True:
    left_motor.set_velocity(controller.axisA.position(), PERCENT)
    right_motor.set_velocity(controller.axisD.position(), PERCENT)

    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)

    wait(20, MSEC)
