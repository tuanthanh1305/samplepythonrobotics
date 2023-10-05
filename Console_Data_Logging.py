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
#    Project:           Console Data Logging
#    Description:       This example will show how to print values
#                       to the Print Console
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
my_variable = 0

# Print 'header' values to the Print Console
print("Timer, Value")

# Print Brain Timer and my_variable values in a loop
while True:
    # Print the values of the Brain Timer and my_variable
    # in a single, comma-separated line to the Print Console
    print("{:.2f}, {:d}".format(brain.timer.time(SECONDS), my_variable))

    # Increment the value of my_variable
    my_variable += 1

    # Add a 200ms delay to avoid filling the Print Console buffer
    wait(0.2, SECONDS)
