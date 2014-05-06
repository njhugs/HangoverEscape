class NoPath(RuntimeError):
    pass

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
        self.items = data['items']
        self.item_list = []#Added by Luke
        for item in data['items']:#Added by Luke            
            self.item_list.append(Item(item))
            #self.item_list[cntr] = Item(self.items[cntr])#Added by Luke

    def __str__(self):
	list_of_strings = [ str(item) for item in self.items ]
        return "room name: " + self.name + "\ndescription: " + self.description + "\nitems: " +  ", ".join(list_of_strings) # made it so also returns room name b4 desc and items

    def get_name(self): #added a method to return room name
	return self.name
    
    def directionExists(self, data, direction):#Might need to pass self as a peramiter
        if(data[self.name][direction] != None):# data is a dictionary with two dictionaries inside -- each being the room 
            return True
        else:
            return False

class World:
    """A world contains one or more rooms"""

    def __init__(self, data, current_name):
        self.rooms = {}
	counter = 0
        for key,value in data.items():
            self.rooms[key] = Room(data[key], data.keys()[counter]) # give each room a name by getting dict key
	    counter = counter + 1 

        self._current = self.rooms[current_name]

    def __str__(self):
        return "World:\n{0}".format( "\n%%\n".join(
            [ name + ": " + str(room) for name,room in self.rooms.items() ]
        ) )
    def current(self):
        current = staticmethod(current)
    @staticmethod
    def current(self):
        return self._current

    def go(self, data, direction):
        if self._current.directionExists(data, direction):
            self.updateRoom(data, direction)
            return True#Direction exists and was moved
        else:
            return False#Direction does not exist and was not moved.
    
    def updateRoom(self, data, direction):
        newRoom = data[self._current.get_name()][direction] 
	self._current = self.rooms[newRoom] #updates the current room object in the world

    #def commandInput(self, data)
