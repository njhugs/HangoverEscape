#! usr/bin/env python3

import game
import world
import sys

myworld1 = world.World( game.data, 'Bedroom')

for rooms_name, room_object in myworld1.rooms.items():
     for item_object in room_object.item_list:
         if isinstance(item_object, world.Item) == False:
             raise RuntimeError("Object type missmatch in Room.item_list.")

while True:
    print(myworld1.current(myworld1))
    l=sys.stdin.readline()
    command, arguments = l.partition(' ')[::2]
    print('\nNow we\'re about to move\n')
    #myworld1.go(game.data, 'north')
    getattr(myworld1, command)(game.data,arguments.strip())


