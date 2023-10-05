#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_motor = Motor(Ports.PORT1, False)
right_motor = Motor(Ports.PORT6, True)



# Make random actually random
def setRandomSeedUsingAccel():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    urandom.seed(int(xaxis + yaxis + zaxis))
    
# Set random seed 
setRandomSeedUsingAccel()

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------------------------------------------
#
#    Project:           Accurate Turns
#    Description:       This example will turn the robot in different
#                       directions to specific headings and print the
#                       headings
#    Brain Supported:   2nd generation
#    Configuration:     Left Motor in Port 1
#                       Right Motor in Port 6
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate the Inertial Sensor and reset the heading to zero
brain_inertial.calibrate()
while brain_inertial.is_calibrating():
    wait(50, MSEC)

brain_inertial.set_heading(0, DEGREES)

# Set motor velocities to 20% so heading values can be more
# accurately checked as the robot turns
left_motor.set_velocity(20, PERCENT)
right_motor.set_velocity(20, PERCENT)

# Start both left and right motors to turn to the right
left_motor.spin(FORWARD)
right_motor.spin(REVERSE)
wait(0.25, SECONDS)

# Wait until the Inertial Sensor's heading is
# greater than 50 degrees before stopping the motors
while not brain_inertial.heading() > 50:
    wait(20, MSEC)
left_motor.stop()
right_motor.stop()

# Print the Inertial Sensor's current heading to the robot brain's screen
brain.screen.print(brain_inertial.heading())
brain.screen.next_row()
wait(1, SECONDS)

# Start both the left and right motors to turn to the left
left_motor.spin(REVERSE)
right_motor.spin(FORWARD)
wait(0.25, SECONDS)

# Ensure that the robot turns past the 0 degree heading
while not brain_inertial.heading() > 60:
    wait(20, MSEC)

# Wait until the Inertial Sensor's heading is
# less than 180 degrees before stopping the motors
while not brain_inertial.heading() < 180:
    wait(20, MSEC)
left_motor.stop()
right_motor.stop()

# Print the final heading from the Inertial Sensor
brain.screen.print(brain_inertial.heading())
