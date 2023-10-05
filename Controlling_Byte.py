#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
IntakeOptical = Optical(Ports.PORT4)
FrontDistance = Distance(Ports.PORT9)
TopTouchLED = Touchled(Ports.PORT10)
IntakeBumper = Bumper(Ports.PORT3)
IntakeGroup_motor_a = Motor(Ports.PORT5, False)
IntakeGroup_motor_b = Motor(Ports.PORT11, True)
IntakeGroup = MotorGroup(IntakeGroup_motor_a, IntakeGroup_motor_b)
ArmGroup_motor_a = Motor(Ports.PORT6, True)
ArmGroup_motor_b = Motor(Ports.PORT12, False)
ArmGroup = MotorGroup(ArmGroup_motor_a, ArmGroup_motor_b)
controller = Controller()
left_drive_smart = Motor(Ports.PORT1, 1.0, False)
right_drive_smart = Motor(Ports.PORT7, 1.0, True)

drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 200)



# Make random actually random
def setRandomSeedUsingAccel():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    urandom.seed(int(xaxis + yaxis + zaxis))
    
# Set random seed 
setRandomSeedUsingAccel()

def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    brain_inertial.calibrate()
    while brain_inertial.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)



# define variables used for controlling motors based on controller inputs
controller_left_shoulder_control_motors_stopped = True
controller_right_shoulder_control_motors_stopped = True
drivetrain_l_needs_to_be_stopped_controller = False
drivetrain_r_needs_to_be_stopped_controller = False

# define a task that will handle monitoring inputs from controller
def rc_auto_loop_function_controller():
    global drivetrain_l_needs_to_be_stopped_controller, drivetrain_r_needs_to_be_stopped_controller, controller_left_shoulder_control_motors_stopped, controller_right_shoulder_control_motors_stopped, remote_control_code_enabled
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
            # check the buttonLUp/buttonLDown status
            # to control IntakeGroup
            if controller.buttonLUp.pressing():
                IntakeGroup.spin(FORWARD)
                controller_left_shoulder_control_motors_stopped = False
            elif controller.buttonLDown.pressing():
                IntakeGroup.spin(REVERSE)
                controller_left_shoulder_control_motors_stopped = False
            elif not controller_left_shoulder_control_motors_stopped:
                IntakeGroup.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_left_shoulder_control_motors_stopped = True
            # check the buttonRUp/buttonRDown status
            # to control ArmGroup
            if controller.buttonRUp.pressing():
                ArmGroup.spin(FORWARD)
                controller_right_shoulder_control_motors_stopped = False
            elif controller.buttonRDown.pressing():
                ArmGroup.spin(REVERSE)
                controller_right_shoulder_control_motors_stopped = False
            elif not controller_right_shoulder_control_motors_stopped:
                ArmGroup.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_right_shoulder_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller = Thread(rc_auto_loop_function_controller)

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------------------------------------------
# 
#    Project:           Controlling Byte
#    Description:       This program shows how to control Byte's motors with 
#                       the controller events and the drivetrain with 
#                       the configured controller.
#                       The Left up/down controller buttons will control 
#                       the Intake Motor
#                       The Right up/down controller buttons will control 
#                       the Arm Motor
#                       The Joysticks are configured for Tank control
#    Brain Supported:   2nd generation
#    Configuration:     VIQC 2023 Byte (Drivetrain 2-motor, Controller)
#                       Drivetrain in Port 1 and Port 7
#                       IntakeOptical in Port 4
#                       FrontDistance in Port 9
#                       TopTouchLED in Port 10
#                       IntakeBumper in Port 3
#                       IntakeGroup in Port 5 and Port 11 reversed
#                       ArmGroup in Port 6 reversed and Port 12
#                       Controller
# ------------------------------------------------------------------------------

# Library imports
from vex import *


# Begin project code
# Callback function when Controller buttonRUp is pressed
def on_R_up_pressed():
    ArmGroup.spin(FORWARD)

    while controller.buttonRUp.pressing():
        # Wait until buttonRUp is released
        wait(20, MSEC)

    ArmGroup.stop()

# Callback function when Controller buttonLUp is pressed
def on_L_up_pressed():
    IntakeGroup.spin(FORWARD)

    while controller.buttonLUp.pressing():
        # Wait until buttonLUp is released
        wait(20, MSEC)

    IntakeGroup.stop()

# Callback function when Controller buttonRDown is pressed
def on_R_down_pressed():
    ArmGroup.spin(REVERSE)

    while controller.buttonRDown.pressing():
        # Wait until buttonRDown is released
        wait(20, MSEC)
    ArmGroup.stop()

# Callback function when Controller buttonLDown is pressed
def on_L_down_pressed():
    IntakeGroup.spin(REVERSE)

    while controller.buttonLDown.pressing():
        # Wait until buttonLDown is released
        wait(20, MSEC)

    IntakeGroup.stop()

# Register event handlers and pass callback functions
controller.buttonRUp.pressed(on_R_up_pressed)
controller.buttonLUp.pressed(on_L_up_pressed)
controller.buttonRDown.pressed(on_R_down_pressed)
controller.buttonLDown.pressed(on_L_down_pressed)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

# Set default motor stopping behavior
IntakeGroup.set_stopping(HOLD)
ArmGroup.set_stopping(HOLD)
