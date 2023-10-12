#region VEXcode Generated Robot Configuration
from vex import *
import random

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
leftmotor = Motor(Ports.PORT6, False)
rightmotor = Motor(Ports.PORT1, False)



# Make random actually random

    
# Set random seed 


#endregion VEXcode Generated Robot Configuration
error = 0
output = 0

def driveStraight_distance_heading_velocity_kp(driveStraight_distance_heading_velocity_kp__distance, driveStraight_distance_heading_velocity_kp__heading, driveStraight_distance_heading_velocity_kp__velocity, driveStraight_distance_heading_velocity_kp__kp):
    global error, output
    leftmotor.spin_to_position(0, DEGREES)
    rightmotor.spin_to_position(0, DEGREES)
    if driveStraight_distance_heading_velocity_kp__velocity > 0:
        while leftmotor.position(DEGREES) < driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            leftmotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            rightmotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            leftmotor.spin(FORWARD)
            rightmotor.spin(FORWARD)
            wait(20, MSEC)
    else:
        while leftmotor.position(DEGREES) > driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            leftmotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            rightmotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            leftmotor.spin(FORWARD)
            rightmotor.spin(FORWARD)
            wait(20, MSEC)
    leftmotor.stop()
    rightmotor.stop()

def when_started1():
    global error, output
    leftmotor.set_stopping(BRAKE)
    rightmotor.set_stopping(BRAKE)
    wait(2, SECONDS)
    driveStraight_distance_heading_velocity_kp(4000, 0, 60, 2)

when_started1()
