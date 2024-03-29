"""
Modify this code to add two more rooms.
"""
# all our states
STATEROOM = 0
STATECLOSET = 1
STATEHALLWAY = 2
STATEKITCHEN = 3
STATEATTIC = 4
STATEOUTSIDE = 5
STATEDONE = 6

state = STATEROOM  # starting in the room

# Four areas
#First room
startRoomTitle = "A Dark Room"
startRoomDesc = """You are in a dark room and can barely see a hallway to the north.  
A faint light can be seen through the cracks of a closed door to the east."""

# Second Room
closetTitle = "A Small Closet"
closetDesc = """You appear to be in a small enclosed closet.  
A single light bulb illuminates the area.  There is nothing to see.
You can only move west to a room."""

# Third Room
hallwayTitle = "A Long Hallway"
hallwayDesc = """You are in a long dark hallway heading north and south.
To the north, the hallway ends in a door, with light showing behind.
To the south, the faint outline of a room can be seen.
To the west, there is a door with some red stains."""

# Fourth Room
kitchenTitle = "A Messy Kitchen"
kitchenDesc = '''You find yourself in a messy kitchen with the smell of tomatoes.
You can see a long hallway to the east and stairs to the attic to the west.'''

# Fifth Room
atticTitle = "A Dusty Attic"
atticDesc = "You climb the stairs and arrive at the attic. Oh no, it looks like there are a pile of bones in the corner. You can only go east back to the kitchen."

# Sixth Room
outsideTitle = "Outside a Creepy House"
outsideDesc = """You are outside a very creepy house.  Good thing it is light
outside or you would be very scared.  You may enter the house to the south or
walk away from the house to the north."""

# testing if the input is good from the user
def validInput(testString):
    string = testString.lower() # make lower case
    # only four possible commands
    if string == "east" or string == "west" or string == "south" or string == "north":
        return True  # good input
    return False # bad input

# check if our direction is good for the current room
def checkDirection(direction, curState):
    noDir = False  # assuming that direction exists
    dir = direction.lower() #change to lower case
    
    if curState == STATEROOM:   # are we in the room?
        if dir == "east":       # can go east
            curState = STATECLOSET  # to the closet
        elif dir == "north":    # can go north
            curState = STATEHALLWAY # to the hallway
        else:   # can't go anywhere
            noDir = True    # not a good direction
    elif curState == STATEHALLWAY:
        if dir == "north":       # can go north
            curState = STATEOUTSIDE  # to the outside
        elif dir == "south":    # can go south
            curState = STATEROOM # to the room
        elif dir == "west":    # can go west
            curState = STATEKITCHEN # to the kitchen
        else:   # can't go anywhere
            noDir = True    # not a good direction
    elif curState == STATEOUTSIDE:
        if dir == "north":       # can go north
            curState = STATEDONE  # to leave and finish
        elif dir == "south":    # can go south
            curState = STATEHALLWAY # to the hallway
        else:   # can't go anywhere
            noDir = True    # not a good direction
    elif curState == STATECLOSET:
        if dir == "west":       # can go west
            curState = STATEROOM  # to the room
        else:   # can't go anywhere
            noDir = True    # not a good direction
    elif curState == STATEKITCHEN:
        if dir == "east":       # can go east
            curState = STATEHALLWAY  # to the hallway
        elif dir == "west":       # can go west
            curState = STATEATTIC  # to the attic
        else:   # can't go anywhere
            noDir = True    # not a good direction
    elif curState == STATEATTIC:
        if dir == "east":       # can go east
            curState = STATEKITCHEN  # to the kitchen
        else:   # can't go anywhere
            noDir = True    # not a good direction
    elif curState == STATEDONE:
        print("Nothing to see here.") # this shouldn't happen
    else:
        print("Error, invalid state", curState)  # error message
    if noDir == True:  # not a good direction
        print("Sorry, you can't go there from here.")
    return curState  # return the state to update if it has changed

# show the decriptions of the rooms
def showRoom(curState):
    print("="*60)
    # show the room info
    if curState == STATEROOM: 
        print(startRoomTitle)
        print(startRoomDesc)
    # show the hallway info
    elif curState == STATEHALLWAY:
        print(hallwayTitle)
        print(hallwayDesc)
    # show the outside info
    elif curState == STATEOUTSIDE:
        print(outsideTitle)
        print(outsideDesc)
    # show the closet info
    elif curState == STATECLOSET:
        print(closetTitle)
        print(closetDesc)
    # show the kitchen info
    elif curState == STATEKITCHEN:
        print(kitchenTitle)
        print(kitchenDesc)
    # show the attic info
    elif curState == STATEATTIC:
        print(atticTitle)
        print(atticDesc)
    # all done, show that
    elif curState == STATEDONE:
        print("Game Over")
    # something has gone wrong, show
    else:
        print("Error, invalid state", curState)
    print("="*60)
        
#start out game loop
while state != STATEDONE:
    showRoom(state)  # show the room description
    # get the input
    choice = input("Please enter your choice of direction as north, south, east or west:\n")
    if validInput(choice):  # test for good input
        state = checkDirection(choice, state)  # if input is good, check if the direction exists
    else:   # if bad input
        print("You cannot do that here.")
print("Bye bye!!")    # leaving the program
