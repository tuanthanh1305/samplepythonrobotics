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
#    Project:           Turning Accurately
#    Description:       This example will show how to use different drivetrain
#                       turning commands to control the robot
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, Inertial)
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Drivetrain Inertial
calibrate_drivetrain()

# The robot is able to turn continuously until told to stop or do something
# else
drivetrain.turn(RIGHT)
wait(4, SECONDS)
drivetrain.stop()

# A brief delay to observe the result of the turning action
wait(1, SECONDS)
drivetrain.turn_for(LEFT, 180, DEGREES)

# A brief delay to observe the result of the turning action
wait(1, SECONDS)

# A Drivetrain can be used to turn to an exact heading when using a Gyro or
# the Brains Inertial
# based on the sensor's feedback
# This command will point the robot back to a rotation value of 0 (its
# starting orientation) and will determine the fastest direction to turn
drivetrain.turn_to_rotation(0, DEGREES)
