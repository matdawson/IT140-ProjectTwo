#Mathew Dawson

#A dictionary for the Lucky Charms Adventure game
#The dictionary links a room to other rooms
#and linking one item to each room except the Great Hall (start room) and the room containing the villain.
rooms = {
        'Great Hall': {'North': 'Gallery','South': 'Den', 'East': 'Bedroom', 'West': 'Cellar'},
        'Bedroom': {'North': 'Dining Room', 'West': 'Great Hall', 'item': 'Rainbow'},
        'Dining Room':{'South': 'Bedroom', 'item': 'Moon'},
        'Cellar': {'East': 'Great Hall', 'item': 'Star'},
        'Den': {'North': 'Great Hall', 'East':'Lounge', 'West': 'Kitchen', 'item': 'Clover'},
        'Kitchen': {'East': 'Den', 'item': 'Horseshoe'},
        'Gallery': {'South': 'Great Hall', 'East': 'Dungeon', 'item': 'Hourglass'},
        'Dungeon': {'West': 'Gallery', 'item': 'Heart'},
        'Lounge': {'West': 'Den', 'item': 'Count Chocula'} #villain
    }

#Starts the player in the first room of the dictionary
currentRoom = 'Great Hall'
#Tracks whether or not the user has ended the game
exitGame = False
#Declare user's input
userInput = ''
#houses the user's inventory when navigating through the rooms
userInventory = []
#houses the items encountered in the rooms
roomItems = []

#Start of the Game
print('Lucky Charms Adventure Game \r\n' +
      'Collect all 7 Lucky Charms or be defeated by Count Chocula \r\n' +
      'Move commands: go South, go North, go East, go West, exit \r\n' +
      'Add to Inventory: get \'item  name\' ')

while exitGame == False:
    print('--------------------')
    print('You are in the ' + currentRoom)
    print('Inventory: ' + str(userInventory))
    if len(roomItems) > 0:
        for item in roomItems:
            if userInventory.count(item) == 0:
                print('You found a ' + item)
    #stripping and uppercasing user input to aid in validation of room moves and item descriptions
    userInput = input('Enter your move: \r\n>').strip().upper()

    #Validation of user input
    if userInput == 'EXIT':
        print('Thanks for playing the game. Hope you enjoyed playing.')
        #exit Game
        exitGame = True
    #validates if the user requesting an item is inside the current room
    elif len(userInput.split()) == 2 and userInput.split()[0] == 'GET':
        if roomItems.count(userInput.split()[1]) > 0:
            userInventory.append(userInput.split()[1])
        else:
            #user input invalid item not in current room
            print('Invalid item')
    #validates if user is attempting to move to another room
    elif len(userInput.split()) != 2 or userInput.split()[0] != 'GO' and userInput.split()[1] != 'NORTH' and userInput.split()[1] != 'SOUTH' and userInput.split()[1] != 'EAST' and userInput.split()[1] != 'WEST':
        #user input invalid move
        print('Invalid move')
    else:
        #splitting user's input to compare against room keys
        userInput = userInput.split()[1]
        userInputmatch = False
        roomItems = []
        #comparing user's input direction to room keys
        for keys in rooms[currentRoom].keys():
            if keys.upper() == userInput:
                currentRoom = rooms[currentRoom][keys]
                userInputmatch = True
        #checking if current room has the villain and if the user has all 7 items
        for keys in rooms[currentRoom].keys():
            if keys == 'item':
                #room contains villain and user has all 7 items
                if rooms[currentRoom].get('item') == 'Count Chocula' and len(userInventory) == 7:
                    print('Congratulations! You have collected all items and defeated Count Chocula! \r\n' +
                    'Thanks for playing the game. Hope you enjoyed it.')
                    exitGame = True
                #room contains villain and user does not have all 7 items
                elif rooms[currentRoom].get('item') == 'Count Chocula' and len(userInventory) < 7:
                    print('NOM NOM..."I COME TO SUCK YOUR BLOOD" says Count Chocula...GAME OVER!\r\n' +
                         'Thanks for playing the game. Hope you enjoyed it.')
                    exitGame = True
                #otherwise append the item to the room item's list
                else:
                    roomItems.append(rooms[currentRoom].get('item').upper())
        #if input direction from current room is invalid
        if userInputmatch == False:
            print('You can\'t go that way!')
