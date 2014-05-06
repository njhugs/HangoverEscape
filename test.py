#! usr/bin/env python3

import game
import world
import sys

myworld1 = world.World( game.data, 'SURGE 104C')

while True:
    #for line in sys.stdin.getline():
    #    print(line)
    l=sys.stdin.readline()
    sys.stdout.write(l)


print(myworld1.current(myworld1))

#print(myworld1.current(myworld1))
command, arguments = 'go north'.partition(' ')[::2]
getattr(myworld1, command)(game.data,arguments)

#print('\nNow we\'re about to move\n')

#myworld1.go(game.data, 'north')

#myworld1.go(game.data, 'south')

for rooms_name, room_object in myworld1.rooms.items():    
    for item_object in room_object.item_list:
        if isinstance(item_object, world.Item) == False:
            raise RuntimeError("Object type missmatch in Room.item_list.")
            #raise RuntimeError("Raptors attacked!")
