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
#    Project:           Playing Sounds
#    Description:       This program will play different sounds depending on
#                       which button is pressed on the Brain.
#                       A list of supported sounds can be found in the help
#                       for the Brain.playSound() command.
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
        brain.play_sound(SoundType.SIREN)

        # Half-second wait so each sound is only played once
        wait(0.5, SECONDS)
    if brain.buttonDown.pressing():
        brain.play_sound(SoundType.HEADLIGHTS_ON)

        # Half-second wait so each sound is only played once
        wait(0.5, SECONDS)
    if brain.buttonCheck.pressing():
        brain.play_sound(SoundType.WRONG_WAY)

        # Half-second wait so each sound is only played once
        wait(0.5, SECONDS)

    wait(20, MSEC)
