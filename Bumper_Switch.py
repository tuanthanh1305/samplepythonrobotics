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
claw_motor = Motor(Ports.PORT4, False)
arm_motor = Motor(Ports.PORT10, True)
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
#    Project:           Bumper Switch
#    Description:       This example will drive in reverse until the
#                       Bumper Switch comes into contact with an object.
#    Brain Supported:   2nd generation
#    Configuration:     Clawbot (Drivetrain 2-motor, Inertial)
#                       Claw Motor in Port 4
#                       Arm Motor in Port 10
#                       Bumper in Port 8
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# The robot starts off driving in reverse
drivetrain.drive(REVERSE)

# The robot will stop driving when the Bumper Switch is pressed
while not bumper_8.pressing():
    # A brief delay inside of a loop to allow other resources to run
    wait(20, MSEC)
drivetrain.stop()
