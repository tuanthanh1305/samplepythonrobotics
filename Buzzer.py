#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
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
#    Project:           Buzzer
#    Description:       This example continuously plays sounds until the
#                       TouchLED is pressed.
#    Brain Supported:   2nd generation
#    Configuration:     TouchLED in Port 2
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
touchled_2.set_color(Color.RED)

# Keep sounding the buzzer in a loop until the TouchLED is pressed
while not touchled_2.pressing():
    brain.play_sound(SoundType.WRONG_WAY)
    wait(1, SECONDS)

touchled_2.set_color(Color.GREEN)
brain.play_sound(SoundType.TADA)
