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
#    Project:           Detecting Acceleration
#    Description:       This project will show how to use the Brain's Inertial
#                       Sensor to detect acceleration along the X, Y, and
#                       Z-axes to then display either red, green or blue on the
#                       TouchLED depending on which way the BaseBot is tilted.
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

# Use a while loop to keep checking
# the Inertial Sensor's acceleration along the X, Y, and Z-axes
while True:
    if brain_inertial.acceleration(XAXIS) < -0.5:
        # Tilt the front of the BaseBot downwards
        # the TouchLED will be set to red
        touchled_2.set_color(Color.RED)
    elif brain_inertial.acceleration(YAXIS) < -0.5:
        # Tilt the BaseBot on the right side
        # the TouchLED will be set to green
        touchled_2.set_color(Color.GREEN)
    elif brain_inertial.acceleration(ZAXIS) < -0.5:
        # Tilt the BaseBot back to the original position
        # the TouchLED will be set to blue
        touchled_2.set_color(Color.BLUE)
    else:
        # Tilt the front of the BaseBot backwards - the TouchLED will turn off
        touchled_2.set_color(Color.BLACK)
