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
optical_3 = Optical(Ports.PORT3)



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
#    Project:           Detecting Colors
#    Description:       This example will continuously detect colors and
#                       will have the robot react different ways depending
#                       on which color is detected
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#                       Optical in Port 3
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

while True:
    if optical_3.is_near_object() and optical_3.color() == Color.RED:
        # If the Optical Sensor detects red
        # the robot will drive forward three inches
        drivetrain.drive_for(FORWARD, 3, INCHES)
    elif optical_3.is_near_object() and optical_3.color() == Color.BLUE:
        # If the Optical Sensor detects blue
        # the robot will drive backward three inches
        drivetrain.drive_for(REVERSE, 3, INCHES)
    elif optical_3.is_near_object() and optical_3.color() == Color.GREEN:
        # If the Optical Sensor detects green
        # the robot will turn 90 degrees to the right
        drivetrain.turn_for(RIGHT, 90, DEGREES)
    elif optical_3.is_near_object() and optical_3.color() == Color.YELLOW:
        # If the Optical Sensor detects yellow
        # the robot will turn 90 degrees to the left
        drivetrain.turn_for(LEFT, 90, DEGREES)
    else:
        # Print if no color is detected
        brain.screen.print("No Color Detected")
        wait(0.5, SECONDS)

        # Clears the screen if no color is detected
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
    wait(20, MSEC)
