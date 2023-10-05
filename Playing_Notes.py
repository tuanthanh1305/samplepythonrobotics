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
#    Project:           Playing Notes
#    Description:       This program will play different notes depending on
#                       which button is pressed on the Brain.
#                       A list of supported note values can be found
#                       in the help for the brain.play_note() command.
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Loop to keep detecting button presses
while True:
    if brain.buttonUp.pressing():
        # Plays a C whole note
        brain.play_note(3, 0, 1000)

        # Half-second wait so each note is only played once
        wait(0.5, SECONDS)
    if brain.buttonDown.pressing():
        # Plays an E half note
        brain.play_note(3, 2, 500)

        # Half-second wait so each note is only played once
        wait(0.5, SECONDS)
    if brain.buttonCheck.pressing():
        # Plays an A quarter note
        brain.play_note(3, 5, 250)

        # Half-second wait so each note is only played once
        wait(0.5, SECONDS)

    wait(20, MSEC)
