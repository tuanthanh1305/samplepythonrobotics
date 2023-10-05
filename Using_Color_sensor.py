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
color_9 = ColorSensor(Ports.PORT9)



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
#    Project:           Using Color sensor
#    Description:       This example will print out the name, hue, and
#                       brightness of the color that the robot detects to the
#                       Brain screen. If the robot detects color blue,
#                       it will drive forward.
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#                       Color Sensor in Port 9
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# Turn the Color Sensor Lamp on
color_9.set_light(100, PERCENT)
# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

while True:
    # If the robot detects color blue, it will drive forward
    if color_9.is_near_object() and color_9.color() == Color.BLUE:
        drivetrain.drive(FORWARD)
    else:
        drivetrain.stop()

    # Erase the Brain screen at the beginning of the project and set
    # the printing location (cursor) to the top right corner
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    # Print the color name
    if color_9.color() == Color.RED:
        brain.screen.print("Color: Red")
    elif color_9.color() == Color.GREEN:
        brain.screen.print("Color: Green")
    elif color_9.color() == Color.BLUE:
        brain.screen.print("Color: Blue")
    else:
        brain.screen.print("Color: Other")
    brain.screen.next_row()

    # Print the hue of the detected color
    brain.screen.print("Hue:", color_9.hue())
    brain.screen.next_row()

    # Print the brightness of the detected color
    brain.screen.print("Brightness:", color_9.brightness())

    # A brief delay to allow text to be printed without distortion or tearing
    wait(0.05, SECONDS)
