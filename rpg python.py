def showInstructions():
  #This is the main menu and the commands that players can use
  print('''
islandqaurts
============
Commands:
  go [direction]
  get [item]
you were on a cruise and you crashed into and the boat crashed into a rock, you wake up on a island...
''')


def showStatus():
  #shows the players status and where they are
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #shows the players inventory
  print('Inventory : ' + str(inventory))
  #shows items in the room if there is any
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
  if "enemy" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['enemy'])
  print("---------------------------")
  if "desc" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['desc'])
  print("---------------------------")            
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['eat'])
  print("---------------------------")
 
#an inventory, which is initially empty
inventory = []


#a dictionary linking a room to other rooms
rooms = {
        'Middle of island': {
                    'south':'forest',
                    'east':'bay',
                    'north':'infront of the mines',
                    'west': 'house',
                    'desc':'you see a few structures and a forest of trees'
                    },


         'infront of the mines':{
                    'south':'Middle of island',
                    '':'in the mines',
                    'desc':'you approach a mineshaft you see it goes down (if you go "south" you could go in) '},


         'bay':{
                    'east':'in the ocean',
                    'west':'Middle of island',
                    'item':'fishing rod',
                    'desc':'you aproach a fishing bay, you see the waves of the ocean hitting the shore(you might be able to go in the ocean with "east")',
                      },
                      'in the ocean':{
                    ''    
                      },


          'forest':{
                      'east':'forest2',
                      'west':'forest1',
                      'enemy':'sneaky cattle',
                      'desc':'you walk into a forest you hear stomping in the distance...'
                      },
             
          'forest1':{
                        'east':'forest',
                        'item':'apples',
                        'desc':'you stop hearing the stomping (: ,you hear waves hitting the island'
                      },
          'forest2':{
                        'west':'forest',
                        'items':'leaves',
                        'desc':'careful! you hear the stomping louder and the trees are shaking'
                      },
 
          'house':{
                      'east':'Middle of island',
                      'south':'forest1'
                      },
                       
          'in the mines':{
                      'west':'loot mine',
                      'north':'the miners mine',
                      'east':'chest room',
                      'item':'bones',
                      'desc':'you see bones of a human but you cant see anyone but there are other tunnels be carful of which you choose'
                      },
          'loot mine':{
                      'east':'mid of mines',
                      ''
                      },
          'chest room':{
                      'west':'mid of mines',
                      },
          'the miners mine':{
                      'south':'mid of mines',
                      },




                      }


         
       




#start the player in the Middle of island
currentRoom = 'Middle of island'


showInstructions()


#loop forever
while True:


  showStatus()


  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
   
  move = move.lower().split()


  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print("You can't go that way!")


  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print("Can't get " + move[1] + "!")


  if move[0]== 'eat':
    if
