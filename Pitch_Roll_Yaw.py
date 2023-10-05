#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT1, 1.0, False)
right_drive_smart = Motor(Ports.PORT6, 1.0, True)

drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 200)
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

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------------------------------------------
#
#    Project:           Pitch, Roll, Yaw
#    Description:       This project will show how to use the Brain's
#                       Inertial Sensor to detect the orientation angle of
#                       the Brain along the X, Y, and Z-axes in order to
#                       determine pitch, roll, and yaw.
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#                       Left Motor in Port 1
#                       Right Motor in Port 6
#                       TouchLED in Port 2
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

touchled_2.set_brightness(100)

# Use a while loop to keep checking the orientation along the X, Y, and Z-axes
while True:
    # Get the Pitch, Roll, and Yaw values from the Brain Inertial sensor
    inertial_pitch = brain_inertial.orientation(PITCH, DEGREES)
    inertial_roll = brain_inertial.orientation(ROLL, DEGREES)
    inertial_yaw = brain_inertial.orientation(YAW, DEGREES)

    if inertial_pitch > 10 or inertial_pitch < -10:
        # Rotate the BaseBot forward and backward along the Y-axis for pitch
        # TouchLED will turn green when +/- 10 degrees from
        # calibration position along the Y-axis
        touchled_2.set_color(Color.GREEN)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Pitch:", inertial_pitch, precision=1)
        brain.screen.next_row()
        brain.screen.print("Rotation: Y axis")
        wait(0.1, SECONDS)
        brain.screen.clear_screen()
    elif inertial_roll > 10 or inertial_roll < -10:
        # Rotate the BaseBot on its left and right side
        # along the X-axis for roll
        # TouchLED will turn red when +/- 10 degrees from
        # calibration position along the X-axis
        touchled_2.set_color(Color.RED)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Roll:", inertial_roll, precision=1)
        brain.screen.next_row()
        brain.screen.print("Rotation: X axis")
        wait(0.1, SECONDS)
        brain.screen.clear_screen()
    elif inertial_yaw > 10 or inertial_yaw < -10:
        # Turn the BaseBot left and right along the Z-axis for yaw
        # TouchLED will turn blue when +/- 10 degrees from
        # calibration position along the Z-axis
        touchled_2.set_color(Color.BLUE)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Yaw:", inertial_yaw, precision=1)
        brain.screen.next_row()
        brain.screen.print("Rotation: Z axis")
        wait(0.1, SECONDS)
        brain.screen.clear_screen()
    else:
        # Rotate the BaseBot back to it's original calibration position
        touchled_2.set_color(Color.BLACK)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("None")
        brain.screen.next_row()
        wait(0.25, SECONDS)
        brain.screen.clear_row(1)
        brain.screen.set_cursor(brain.screen.row(), 1)
