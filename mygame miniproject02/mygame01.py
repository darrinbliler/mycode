#!/usr/bin/env python3
"""RPG Game"""

from pprint import pprint

def showInstructions():
    """Showing our user instructions"""
    print('''
    RPG Game
    ========
    Commands:
        go [direction]
        get [item]
        Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go direction and get item.''')

def showStatus():
    """determine the current status of the player"""
    print('__________________________')
    print('You are in the ' + currentRoom)
    print('Inventory: ', inventory)
    if "item" in rooms[currentRoom]:
        for item in range(len(rooms[currentRoom]['item'])):  
            print('You see a ' + rooms[currentRoom]['item'][item])
    else:
            "The room is empty."
    print("__________________")

inventory = []

currentRoom = "Hall"

rooms = {
            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : ['key', 'dinosaur']
            },

            'Kitchen' : {
                'north' : 'Hall',
                'item' : ['knife', 'monster']
            },
            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : ['table', 'model train']                    
            },
            'Garden' : {
                'north' : 'Dining Room',
                'item' : ['dolph lundgren statue', 'chainsaw']
            }
        }

showInstructions()

def main():
    currentRoom = "Hall"
    showInstructions()
# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    #print(rooms[currentRoom]['item'].values())
    

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get

        # create a list of items in the current room
        currentRoom_items = rooms[currentRoom]['item']

        if move[1] in currentRoom_items:
            inventory.append(move[1])
            print(move[1] + ' got!')
            room_item_list = rooms[currentRoom]['item']
            item_index_loc = room_item_list.index(move[1])
            del rooms[currentRoom]['item'][item_index_loc]
            print(rooms[currentRoom]['item'])

        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'drop' first
    if move[0] == 'drop':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to drop

        # create a list of items in the current room
        currentRoom_items = rooms[currentRoom]['item']

        if move[1] in currentRoom_items:
            #room_item_list = rooms[currentRoom]['item']
            #item_index_loc = room_item_list.index[move[1]]
            inventory = inventory.remove(move[1])
            print(inventory)
            print(move[1] + ' dropped!')

if __name__ == "__main__":
    main()  