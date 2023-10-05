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
#    Project:           Drivetrain Sensing
#    Description:       This example will print Drivetrain-related
#                       information to the IQ Brain's Screen
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# Reset Rotation and Heading values
drivetrain.set_heading(0, DEGREES)
drivetrain.set_rotation(0, DEGREES)

# Change the font size to fit on the IQ (2nd generation) Brain's Screen
brain.screen.set_font(FontType.MONO12)

drivetrain.drive(FORWARD)

# Print Drivetrain Sensing values in a loop
while True:
    # Clear the screen and reset the print cursor to the top left corner
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    brain.screen.print("Velocity:", drivetrain.velocity(RPM))
    brain.screen.next_row()

    brain.screen.print("Current:", drivetrain.current(CurrentUnits.AMP))
    brain.screen.next_row()

    brain.screen.print("Rotation:", drivetrain.rotation(DEGREES))
    brain.screen.next_row()

    brain.screen.print("Heading:", drivetrain.heading(DEGREES))
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(0.2, SECONDS)
