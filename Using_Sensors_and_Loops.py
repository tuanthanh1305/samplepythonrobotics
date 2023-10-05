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
#    Project:           Using Sensors and Loops
#    Description:       This example will use the arm motor sensing commands
#                       to determine the angle to move the arm motor
#    Brain Supported:   2nd generation
#    Configuration:     Clawbot (Drivetrain 2-motor, Inertial)
#                       Claw Motor in Port 4
#                       Arm Motor in Port 10
#
# ------------------------------------------------------------------------------

# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# Drive the robot forward towards an object
drivetrain.drive_for(FORWARD, 200, MM)

# Spin the Arm Motor forward while the Motor angle is less than 90 degrees
while arm_motor.position(DEGREES) < 90:
    arm_motor.spin(FORWARD)
    # A brief delay inside of a loop to allow other resources to run
    wait(20, MSEC)

# Spin the Arm Motor reverse while the Motor angle is greater than 10 degrees
while arm_motor.position(DEGREES) > 10:
    arm_motor.spin(REVERSE)
    # A brief delay inside of a loop to allow other resources to run
    wait(20, MSEC)

# Once the Arm Motor reaches an angle of less than 10 degrees
# Stop the Arm Motor
arm_motor.stop()
