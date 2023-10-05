#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT1, 1.0, False)
right_drive_smart = Motor(Ports.PORT6, 1.0, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 200, 173, 76, MM, 1)
gyro_5 = Gyro(Ports.PORT5)



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
#    Project:           Gyro Sensing
#    Description:       This example will show all of the available commands
#                       for using the Gyro Sensor
#    Brain Supported:   2nd generation
#    Configuration:     BaseBot (Drivetrain 2-motor, No Gyro)
#                       Gyro in Port 5
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Calibrate and reset the values for the Gyro
gyro_5.calibrate(GyroCalibrationType.NORMAL)
gyro_5.set_heading(0, DEGREES)
gyro_5.set_rotation(0, DEGREES)

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

# Print all Gyro sensing values to the screen in an infinite loop
while True:
    # Clear the screen and set the cursor to top left corner on each loop
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    brain.screen.print("Heading:",
                       gyro_5.heading(), "degrees")
    brain.screen.next_row()

    brain.screen.print("Rotation:",
                       gyro_5.rotation(), "degrees")
    brain.screen.next_row()

    brain.screen.print("Rate:",
                       gyro_5.rate(), "dps")
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(0.2, SECONDS)
