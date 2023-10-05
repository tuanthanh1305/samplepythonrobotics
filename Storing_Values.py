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
#    Project:           Storing Values
#    Description:       This example will show how variables
#                       can be used to store values for later use
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor)
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# Variables can be used to set specific values to be used later in your project
distance_to_travel = 250
angle_to_turn = 90

drivetrain.drive_for(FORWARD, distance_to_travel, MM)
drivetrain.turn_for(RIGHT, angle_to_turn, DEGREES)

# Variable values can be changed at any point in your project
distance_to_travel = 150
angle_to_turn = 45
drivetrain.drive_for(FORWARD, distance_to_travel, MM)
drivetrain.turn_for(RIGHT, angle_to_turn, DEGREES)

# Variable values can also be used to increment a variable
distance_to_travel += 100
angle_to_turn += 90
drivetrain.drive_for(FORWARD, distance_to_travel, MM)
drivetrain.turn_for(RIGHT, angle_to_turn, DEGREES)
