import random

class Hold_item:
    """A single hold item"""
    
    def __init__(self, hiName, hiLocation):
        self.name = hiName
        self._location = hiLocation
        self._found = False

    def __str__(self):
        return self.name
        
    def get_location(self):
        return self._location

    def get_found(self):
        return self._found

    def set_found(self, found):
        self._hifound = found 
        
class Item:
    """A signle item"""

    def __init__(self, item_name):
        self.name = item_name

    def __str__(self):
        return self.name

class Room:
    """A single room"""

    def __init__(self, data, name):
        self.name = name #added a name attribute
        self.description = data['desc']
        self.items = data['objects'] # list of item string names
        self.item_list = [] # list of room objects
        for item in data['objects']:#Added by Luke            
            self.item_list.append(Item(item))
            #self.item_list[cntr] = Item(self.items[cntr])#Added by Luke

    def __str__(self):
        list_of_strings = [ str(item) for item in self.items ]
        return "room name: " + self.name + "\ndescription: " + self.description + "\nobjects: " +  ", ".join(list_of_strings) # made it so also returns room name b4 desc and items

    def get_name(self): #added a method to return room name
        return self.name
    
class World:
    """A world contains one or more rooms"""

    def __init__(self, data, current_name):
        self.rooms = {}
        counter = 0
        for key,value in data.items():
            self.rooms[key] = Room(data[key], data.keys()[counter]) # give each room a name by getting dict key
            counter = counter + 1

	self.inventory = [] # the items the player has found 

        #rndRooms = {}
        #print("This is a random room: " + random.choice(random.choice(self.rooms.keys()).item_list) )
        #self._wallet = Hold_item( 'wallet', 'bed' )
        #self._wallet = Hold_item( 'wallet', random.choice(random.choice(self.rooms.keys()).item_list))

        #self._keys = Hold_item( 'keys', random.choice(random.choice(self.rooms.keys()).item_list.keys()) )
        #self._phone = Hold_item( 'phone', random.choice(random.choice(self.rooms.keys()).item_list.keys()) )

        self._current = self.rooms[current_name]
        #randamize and intitialize items here

    def __str__(self):
        return "World:\n{0}".format( "\n%%\n".join(
            [ name + ": " + str(room) for name,room in self.rooms.items() ]
        ) )
    def current(self):
        current = staticmethod(current)

    @staticmethod
    def current(self):
        return self._current

    def go(self, data, direction): # put a try, except in for accessing direction
        try:
            newRoom = data[self._current.get_name()][direction]
        except KeyError:
            print("\nYou can't go: " + direction + "\n") 
        else:
            self._current = self.rooms[newRoom] #updates the current room object in the world   

    def search(self, data, object): #search only current room
        try:
            object_desc = data[self._current.get_name()][object] # this assumes one item per object
        except KeyError: # there's no object with that name
            print("There is no \"" + object + "\" in this room.")
        else:
            self.inventory.append(object_desc)
                
	    print(object_desc) 
     
class NoPath(KeyError):
     def __init__(self, direction):
        self.direction = direction
     def __str__(self):
        return ("There is no path leading " + self.direction)
   #def commandInput(self, data)
