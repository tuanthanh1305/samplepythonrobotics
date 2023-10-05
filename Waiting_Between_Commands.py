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
#    Project:           Waiting Between Commands
#    Description:       This example will show how to use the wait
#                       command to control the flow of your project
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# 'Non-Waiting' commands like 'drive' will move the robot until told otherwise
drivetrain.drive(FORWARD)
wait(2, SECONDS)

# After 2 seconds, the drivetrain is now told to stop for 3 seconds
drivetrain.stop()
wait(3, SECONDS)

# 'Waiting' commands like 'turn for' will stop the robot
# after the movement is completed
drivetrain.turn_for(RIGHT, 90, DEGREES)
wait(0.5, SECONDS)

# Adding a wait after a 'Waiting' command can help
# observe discrete robot behaviors
drivetrain.drive_for(FORWARD, 200, MM, wait=False)
wait(2, SECONDS)

# Here, even though the 'drive for' is 'Non-Waiting', the added wait
# will ensure that "Done Driving" will only be printed after the robot stops
brain.screen.print("Done Driving")
