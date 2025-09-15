class Room():
    def __init__(self, room_description, character=None, item=None, locked=[False, None, None]):
        self.description = room_description
        self.linked_rooms = {}
        self.character = character
        self.item = item
        self.locked = locked
        self.key = locked[1]
        self.locked_text = locked[2]

    def set_name(self, room_name):
        self.name = room_name

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def lock(self):
        self.locked = True
    
    def unlocked(self):
        self.locked = False
    
    def set_key(self, condition):
        self.locked_text = condition

    def link(self, room_to_link, direction):
        compliments = {
            'north': 'south',
            'south': 'north',
            'east': 'west',
            'west': 'east',
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        self.linked_rooms[direction] = room_to_link
        room_to_link.linked_rooms[compliments[direction]] = self
    
    def display_room(self):
        print(self.description)
        print()
    
    def display_item(self):
        if self.item:
            print()
            print(self.item.description)

    def display_character(self):
        if self.character:
            print()
            print(self.character.description)

    def display_exits(self):
        print()
        print(f"Possible exits: {', '.join(list(self.linked_rooms.keys()))}")
    
    def move(self, direction):
        if direction in self.linked_rooms:
            destination = self.linked_rooms[direction]
            if not destination.locked:
                text = f'You move {direction}'
                return destination
            else:
                return self        
        else:
            text = f"You failed to move {direction}."
            return self

class Character():
    def __init__(self, character_description, item, success_text, hint):
        self.description = character_description
        self.room = None
        self.item = item
        self.success_text = success_text
        self.hint = hint

    def set_description(self, description):
        self.description = description
    
    def set_item(self, item):
        self.item = item
    
    def set_success_text(self, text):
        self.success_text = text
    
    def set_hint(self, text):
        self.hint = text
    
    def set_room(self, room):
        self.room = room

    
class Item():
    def __init__(self, name, description, use_text):
        self.name = name
        self.description = description
        self.use_text = use_text