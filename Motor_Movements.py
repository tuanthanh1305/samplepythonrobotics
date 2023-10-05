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
#    Project:           Motor Movements
#    Description:       This example will show the different commands
#                       available to control a motor
#    Brain Supported:   2nd generation
#    Configuration:     Clawbot (Drivetrain 2-motor, Inertial)
#                       Claw Motor in Port 4
#                       Arm Motor in Port 10
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Motors can spin forever until told to stop
arm_motor.spin(FORWARD)
wait(3, SECONDS)
arm_motor.stop()

# Motors can also spin for a distance based on the current position
arm_motor.spin_for(REVERSE, 90, DEGREES)

# Motors can also spin to a specific rotation position
arm_motor.spin_to_position(90, DEGREES)

# Motor positions can be reset (set to zero) or set to any value
arm_motor.set_position(0, DEGREES)

# Motors can change velocity (speed)
arm_motor.set_velocity(50, PERCENT)

# Motors can change their behavior when told to stop
# BRAKE - Motor will act like a brake to slow motion even faster
# COAST - No power applied when stopping
# HOLD - Motor will hold its current position against external forces
arm_motor.set_stopping(BRAKE)
arm_motor.set_max_torque(50, PERCENT)
arm_motor.set_timeout(1, SECONDS)
arm_motor.spin_to_position(360, DEGREES)
arm_motor.stop()
