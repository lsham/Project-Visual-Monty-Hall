## Written by: Liam Shamir
## Project: Monty Hall Problem (with GUI)

## Explanation/Purpose: The purpose of this project is to either run the
## Monty Hall problem via a GUI where the user can choose what they want to
## do OR enable the user to run the simulation an inputed number of times
## to figure out if it is statistically better to switch doors or not.


## -------------------------------------------------------------------------- ##
from random import randint


def setupDoors():
    """The purpose of this function is to setup the door layout for the problem."""
    num = randint(1,3)
    ## The following if statement will determine which door has a car (1) and
    ## which has a goat (0).
    if num == 1:
        door1 = 1
        door2 = 0
        door3 = 0
        doors = [1,0,0]
        break
    elif num == 2:
        door1 = 0
        door2 = 1
        door3 = 0
        doors = [0,1,0]
        break
    else:
        door1 = 0
        door2 = 0
        door3 = 1
        doors = [0,0,1]
        break
    return door1,door2,door3,doors

def pickMontyDoor(door1,door2,door3,doors,PlayerDoor):
    """This function will pick which door Monty will reveal."""
    MontyDoor = randint(1,3)
    while MontyDoor == PlayerDoor:
        MontyDoor = randint(1,3)
    ## With the Monty's door selected, we must now make sure he didnt pick the same
    ## door as the Player as well as with the car behind it.
    unchosenDoor = [1,2,3]
    unchosenDoor.pop((PlayerDoor - 1))
    unchosenDoor.pop((MontyDoor - 1))
        
