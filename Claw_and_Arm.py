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
#    Project:           Claw and Arm
#    Description:       This example will show how to use Clawbot to
#                       grab an object and transports it forward.
#                       The Clawbot then places the object
#                       down and returns to its original spot.
#    Brain Supported:   2nd generation
#    Configuration:     Clawbot (Drivetrain 2-motor, Inertial)
#                       Claw Motor in Port 4
#                       Arm Motor in Port 10
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# Set the Arm stopping to hold mode
arm_motor.set_stopping(HOLD)

# Set the encoder values of both the Arm and Claw motor
# encoders to zero
claw_motor.set_position(0, DEGREES)
arm_motor.set_position(0, DEGREES)

# set motion timeout to prevent damage to the Arm/Claw
# if the object is too large
claw_motor.set_timeout(1, SECONDS)
arm_motor.set_timeout(1, SECONDS)

# Close the Claw on an object
claw_motor.spin_for(FORWARD, 30, DEGREES)
wait(1, SECONDS)

# Raise the Arm
arm_motor.spin_for(FORWARD, 1, TURNS)

# Drive Forward
drivetrain.drive_for(FORWARD, 10, INCHES)

# Lower the Arm
arm_motor.spin_for(REVERSE, 1, TURNS)

# Open the Claw
claw_motor.spin_for(REVERSE, 30, DEGREES)

# Move the robot back to the original starting place
wait(1, SECONDS)
drivetrain.drive_for(REVERSE, 10, INCHES)
