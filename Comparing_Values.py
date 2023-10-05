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
#    Project:           Comparing Values
#    Description:       This program looks at the variable to see if
#                       it is greater than or less than 10.
#                       The message on the screen is updated according to
#                       that value.
#                       If the value of the variable is greater than 10,
#                       the program will print 'Value is more than 10'
#                       on the screen.
#                       If the value of the variable is less than 10,
#                       the program will print, 'Value is less than 10'
#                       on the screen.
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
# Change the font size to fit on the IQ (2nd generation) Brain's screen
brain.screen.set_font(FontType.MONO12)

my_variable = 0
for repeat_count in range(20):
    # Clearing the screen and resetting the cursor
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    # Display the current value of the variable
    brain.screen.print("my_variable:", my_variable)
    brain.screen.next_row()

    # Checks to see if the variable is equal to 10
    if my_variable == 10:
        brain.screen.print("Value equals 10")

    # Checks to see if the variable is greater than 10
    if my_variable > 10:
        brain.screen.print("Value is more than 10")

    # Checks to see if the variable is less than 10
    if my_variable < 10:
        brain.screen.print("Value is less than 10")

    wait(1, SECONDS)

    # Adding one to the current variable value
    my_variable += 1
