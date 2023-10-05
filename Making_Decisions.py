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
bumper_8 = Bumper(Ports.PORT8)



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
#    Project:           Making Decisions
#    Description:       This example will use a Bumper Sensor to
#                       detect when the robot has driven into a wall or surface
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#                       Bumper in Port 8
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# A 'while True' loop will cause the following
# set of commands to repeat forever
while True:
    if bumper_8.pressing():
        # An 'if' statement to stop driving if the Bumper is pressed
        drivetrain.stop()
    else:
        # And the else condition will drive reverse if
        # the Bumper is not pressed
        drivetrain.drive(REVERSE)

    # A brief delay inside of a repeating loop to allow other resources to run.
    wait(20, MSEC)
