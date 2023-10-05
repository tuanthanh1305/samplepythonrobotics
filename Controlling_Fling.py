#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT1, 1.0, True)
right_drive_smart = Motor(Ports.PORT3, 1.0, False)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 200, 260, 76, MM, 1)
bumper_sensor = Bumper(Ports.PORT5)
catapult_motor = Motor(Ports.PORT4, True)
intake_motor = Motor(Ports.PORT2, True)
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



# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller = False
drivetrain_r_needs_to_be_stopped_controller = False

# define a task that will handle monitoring inputs from controller
def rc_auto_loop_function_controller():
    global drivetrain_l_needs_to_be_stopped_controller, drivetrain_r_needs_to_be_stopped_controller, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axisA
            # right = axisD
            drivetrain_left_side_speed = controller.axisA.position()
            drivetrain_right_side_speed = controller.axisD.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller = Thread(rc_auto_loop_function_controller)

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------------------------------------------
#
#    Project:           Controlling Fling
#    Description:       This program shows how to control Fling's motors with
#                       the controller events and the drivetrain with
#                       the configured controller.
#                       The Left up/down controller buttons will control
#                       the Intake Motor
#                       The Right up/down controller buttons will control
#                       the Catapult Motor
#                       The Joysticks are configured for Tank control
#    Brain Supported:   2nd generation
#    Configuration:     VIQC 2021 Fling (Drivetrain 2-motor, Reversed)
#                       Drivetrain in Ports 1 and 3
#                       Bumper in Port 5
#                       Catapult Motor in Port 4
#                       Intake Motor in Port 2
#                       Controller
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *


# Begin project code
# Callback function when Controller buttonLDown is pressed
def on_L_down_pressed():
    intake_motor.spin(FORWARD)

    while controller.buttonLDown.pressing():
        # Wait until buttonLDown is released
        wait(20, MSEC)

    intake_motor.stop()


# Callback function when Controller buttonLUp is pressed
def on_L_up_pressed():
    intake_motor.spin(REVERSE)

    while controller.buttonLUp.pressing():
        # Wait until buttonLUp is released
        wait(20, MSEC)

    intake_motor.stop()


# Callback function when Controller buttonRDown is pressed
def on_R_down_pressed():
    catapult_motor.spin(FORWARD)

    while controller.buttonRDown.pressing():
        # Wait until buttonRDown is released
        wait(20, MSEC)

    catapult_motor.stop()


# Callback function when Controller buttonRUp is pressed
def on_R_up_pressed():
    catapult_motor.spin(REVERSE)

    while controller.buttonRUp.pressing():
        # Wait until buttonRUp is released
        wait(20, MSEC)

    catapult_motor.stop()


# Register event handlers and pass callback functions
controller.buttonLUp.pressed(on_L_up_pressed)
controller.buttonRDown.pressed(on_R_down_pressed)
controller.buttonRUp.pressed(on_R_up_pressed)
controller.buttonLDown.pressed(on_L_down_pressed)

# Set default motor stopping behavior
catapult_motor.set_stopping(HOLD)
catapult_motor.set_stopping(HOLD)
