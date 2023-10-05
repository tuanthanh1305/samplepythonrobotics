#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
optical_3 = Optical(Ports.PORT3)



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
#    Project:           Using Optical Sensor
#    Description:       This example will print out the name, hue, and
#                       brightness of the color that the Optical Sensor detects
#                       to the Brain screen.
#    Brain Supported:   2nd generation
#    Configuration:     Optical Sensor in Port 3
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Turn the Optical Sensor Lamp on
optical_3.set_light(LedStateType.ON)

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

while True:
    # Erase the Brain screen at the beginning of the project and set
    # the printing location (cursor) to the top left corner
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    # We want to only get information from the sensor if the object is found
    if optical_3.is_near_object():
        brain.screen.print("Object found")
        brain.screen.next_row()

        # Use the if/elif/else statements to print the
        # color detected by the Optical Sensor
        if optical_3.color() == Color.RED:
            brain.screen.print("Detects: red")
        elif optical_3.color() == Color.GREEN:
            brain.screen.print("Detects: green")
        elif optical_3.color() == Color.BLUE:
            brain.screen.print("Detects: blue")
        elif optical_3.color() == Color.YELLOW:
            brain.screen.print("Detects: yellow")
        elif optical_3.color() == Color.ORANGE:
            brain.screen.print("Detects: orange")
        elif optical_3.color() == Color.PURPLE:
            brain.screen.print("Detects: purple")
        elif optical_3.color() == Color.CYAN:
            brain.screen.print("Detects: cyan")
        else:
            brain.screen.print("Unknown color")
        brain.screen.next_row()

        brain.screen.print("Brightness:", optical_3.brightness())
        brain.screen.next_row()

        brain.screen.print("Hue:", optical_3.hue())
    else:
        # If an object is not found, we may be getting incorrect values
        brain.screen.print("No object found")

    # A brief delay to allow text to be printed without distortion or tearing
    wait(0.2, SECONDS)
