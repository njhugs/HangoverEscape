#!/usr/bin/env python3

import world
import yaml

data = yaml.load( open('rooms.yaml', 'r') )

myworld = world.World( data, 'SURGE 104C' )
