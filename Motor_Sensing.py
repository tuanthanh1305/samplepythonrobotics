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
#    Project:           Motor Sensing
#    Description:       This example will show all of the available commands
#                       for getting Motor Sensing values
#    Brain Supported:   2nd generation
#    Configuration:     Clawbot (Drivetrain 2-motor, Inertial)
#                       Left Motor in Port 1
#                       Right Motor in Port 6
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# Change the font size to fit on the IQ (2nd generation) Brain's Screen
brain.screen.set_font(FontType.MONO12)

arm_motor.spin(FORWARD)

# A 'while' loop will cause the following set of commands to repeat
# until the Arm is lifted
while arm_motor.position(DEGREES) < 300:
    # Clear the screen and reset the print cursor to the top left corner
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    brain.screen.print("Velocity:", arm_motor.velocity(RPM))
    brain.screen.next_row()

    brain.screen.print("Current:", arm_motor.current(CurrentUnits.AMP))
    brain.screen.next_row()

    brain.screen.print("Position:", arm_motor.position(DEGREES))
    brain.screen.print(" degrees")
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(0.2, SECONDS)

# After the condition of the loop is met, the loop breaks,
# and the Arm Motor stops
arm_motor.stop()
