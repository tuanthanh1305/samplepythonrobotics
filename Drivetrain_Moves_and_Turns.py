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
#    Project:           Drivetrain Moves and Turns
#    Description:       This example uses the drivetrain to drive
#                       and turn in different directions
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the drivetrain for accurate turning
calibrate_drivetrain()

# Driving Forward and Turning Right
drivetrain.drive_for(FORWARD, 200, MM)
drivetrain.turn_for(RIGHT, 90, DEGREES)

# Driving Forward and Turning Left
drivetrain.drive_for(FORWARD, 200, MM)
drivetrain.turn_for(LEFT, 90, DEGREES)

# Driving Reverse and Turning Left
drivetrain.drive_for(REVERSE, 200, MM)
drivetrain.turn_for(LEFT, 90, DEGREES)

# Driving Forward and Turning Right
drivetrain.drive_for(FORWARD, 200, MM)
drivetrain.turn_for(RIGHT, 90, DEGREES)
