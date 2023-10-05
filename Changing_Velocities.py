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
#    Project:           Changing Velocities
#    Description:       This example demonstrates how to change the speed
#                       of a drivetrain's drive and turn actions.
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the drivetrain for accurate turning
calibrate_drivetrain()

# Drives robot forward 6 inches at the default 50% velocity
drivetrain.drive_for(FORWARD, 6, INCHES)
wait(1, SECONDS)

# Drives the robot in reverse for 6 inches at 90% velocity
drivetrain.set_drive_velocity(90, PERCENT)
drivetrain.drive_for(REVERSE, 6, INCHES)
wait(1, SECONDS)

# Turns the robot 90 degrees to the right at the default 50% velocity
drivetrain.turn_for(RIGHT, 90, DEGREES)
wait(1, SECONDS)

# Turns the robot to the left at 25% velocity
drivetrain.set_turn_velocity(25, PERCENT)
drivetrain.turn_for(LEFT, 90, DEGREES)
