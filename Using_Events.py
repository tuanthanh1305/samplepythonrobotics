#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()



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
#    Project:           Using Events
#    Description:       This example will show how events work by triggering
#                       an event when the IQ Brain's check button is pressed
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
check_press_count = 0


def check_button_press():
    global check_press_count
    # Change the font size to fit on the IQ (2nd generation) Brain's screen
    brain.screen.set_font(FontType.MONO12)

    brain.screen.clear_row(3)
    brain.screen.set_cursor(3, 1)
    check_press_count += 1

    # Prints the number of times the Brain's check button is pressed
    brain.screen.print("Check Presses:", check_press_count, precision=0)
    brain.timer.clear()


# Checks if the Brain's check button is pressed.
# then calls the callback function.
brain.buttonCheck.pressed(check_button_press)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

while True:
    brain.screen.clear_row(1)
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Timer:", brain.timer.time(SECONDS), precision=2)

    # Brief wait to prevent print tearing
    wait(0.02, SECONDS)
