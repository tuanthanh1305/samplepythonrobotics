#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
distance_7 = Sonar(Ports.PORT7)



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
#    Project:           Distance Sensing (1st gen sensor)
#    Description:       This example will show how to use all of the available
#                       commands using the Distance (1st gen sensor).
#    Brain Supported:   2nd generation
#    Configuration:     Distance (1st gen sensor) in Port 7
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

# Loop to print all distance sensing values to the screen
while True:
    # Clear the screen and set cursor to top left corner of the screen
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    brain.screen.print("Found Object:",
                       "TRUE" if distance_7.is_object_detected() else "FALSE")
    brain.screen.next_row()

    brain.screen.print("Distance - mm:", distance_7.distance(MM))
    brain.screen.next_row()

    brain.screen.print("Distance - in:", distance_7.distance(INCHES))
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(0.2, SECONDS)
