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
#    Project:           Using Threads
#    Description:       This example will show how to run multiple
#                       threads (tasks) in a project at the same time
#    Brain Supported:   2nd generation
#    Configuration:     None
#
# ------------------------------------------------------------------------------

# Library imports
from vex import *


# Begin project code
def second_thread_time_delay(time_delay):
    second_thread_count = 0
    brain.screen.set_font(FontType.MONO12)
    while True:
        brain.screen.set_cursor(3, 1)
        brain.screen.print("500ms Loop:", second_thread_count)

        second_thread_count += 1
        wait(time_delay, SECONDS)


def thread_2():
    # This thread runs a function
    # The function takes timeDelay in seconds as a parameter
    second_thread_time_delay(0.5)


def thread_1():
    # Second thread
    first_thread_count = 0
    brain.screen.set_font(FontType.MONO12)
    while True:
        brain.screen.set_cursor(2, 1)
        brain.screen.print("250ms Loop:", first_thread_count)

        first_thread_count += 1
        wait(0.25, SECONDS)


my_thread_1 = Thread(thread_1)
my_thread_2 = Thread(thread_2)

# Default/main thread
main_thread_count = 0

brain.screen.set_font(FontType.MONO12)
while True:
    brain.screen.set_cursor(1, 1)
    # Print from the main thread to show that it is running
    # at the same time as other threads
    brain.screen.print("100ms Loop:", main_thread_count)

    main_thread_count += 1
    wait(0.1, SECONDS)
