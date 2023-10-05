#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
bumper_8 = Bumper(Ports.PORT8)
touchled_2 = Touchled(Ports.PORT2)



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
#    Project:           Complex Decisions (and, or, not)
#    Description:       This example will use logical operators to create
#                       complex decisions based on multiple sensor inputs
#    Brain Supported:   2nd generation
#    Configuration:     Bumper in Port 8
#                       TouchLED in Port 2
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code

# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO15)

# Place your conditionals in a while (true) loop
# to keep the sensors checking for new events.
while True:
    # Clear the Brain's screen and place the cursor at row one, column one.
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    # The 'and' operator requires BOTH conditions to be "True"
    # for the conditional statement to evaluate as "True"
    brain.screen.print("AND Statement:",
                       bumper_8.pressing() and touchled_2.pressing())

    # Move the cursor to the next line
    brain.screen.next_row()

    # The 'or' operator requires EITHER condition to be "True"
    # for the conditional statement to evaluate as "True"
    brain.screen.print("OR Statement:",
                       bumper_8.pressing() or touchled_2.pressing())

    # Move the cursor to the next line
    brain.screen.next_row()

    # The 'not' operator will return the inverse (opposite) value
    brain.screen.print("NOT Statement:", not bumper_8.pressing())

    # A brief delay to allow text to be printed without distortion or tearing
    wait(0.03, SECONDS)
