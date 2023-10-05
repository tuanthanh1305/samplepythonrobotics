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
#    Project:           Controller Buttons
#    Description:       This program shows two different ways of
#                       controlling robot behavior using Controller buttons.
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

    # Spinning the arm_motor forward raises the arm
    arm_motor.spin(FORWARD)

    while controller.buttonLUp.pressing():
        # Wait until Controller ButtonLUp is released
        wait(20, MSEC)

    arm_motor.stop()


# Callback function when Controller buttonLDown is pressed
def on_L_down_pressed():

    # Spinning the arm_motor in reverse lowers the arm
    arm_motor.spin(REVERSE)

    while controller.buttonLDown.pressing():
        # Wait until Controller ButtonLDown is released
        wait(20, MSEC)

    arm_motor.stop()


# Register event handlers and pass callback functions
controller.buttonLUp.pressed(on_L_up_pressed)
controller.buttonLDown.pressed(on_L_down_pressed)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

# Set default motor stopping behavior and velocity
arm_motor.set_stopping(HOLD)
claw_motor.set_stopping(HOLD)
arm_motor.set_velocity(60, PERCENT)
claw_motor.set_velocity(30, PERCENT)

# Loop to keep checking for Controller R Up and R Down button presses
while True:
    if controller.buttonRUp.pressing():
        # Spinning the claw_motor forward closes the claw
        claw_motor.spin(FORWARD)
    elif controller.buttonRDown.pressing():
        # Spinning the claw_motor in reverse opens the claw
        claw_motor.spin(REVERSE)
    else:
        # Stop the claw_motor if buttonRUp is not pressed
        claw_motor.stop()
    wait(20, MSEC)
