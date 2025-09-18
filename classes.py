class Room():
    def __init__(self, room_description, character=None, item=None, locked=[False, None, None]):
        self.description = room_description
        self.linked_rooms = {}
        self.character = character
        if self.character:
            self.character.room = self
        self.item = item
        self.locked = locked[0]
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
    
    def unlock(self):
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
        print()
        print(self.description)
        if self.item:
            print()
            print(self.item.description)
        if self.character:
            print()
            print(self.character.description)

    def display_exits(self):
        print()
        print(f"Possible exits: {', '.join(list(self.linked_rooms.keys()))}")
        print()
    
    def move(self, direction):
        if direction in self.linked_rooms:
            destination = self.linked_rooms[direction]
            if not destination.locked:
                text = f'You move {direction}'
                return (destination, text)
            else:
                if destination.key.room.character == destination.key:
                    return (self, destination.locked_text)
                else:
                    destination.unlock()
                    text = f'You move {direction}'
                    return (destination, text)
        else:
            text = f"You failed to move {direction}."
            return (self, text)

class Lockbox(Room):
    def __init__(self, room_description, character=None, item=None, locked=[False, None, None], code=None):
        super().__init__(room_description, character, item, locked)
        self.code = code

    def attempt_code(self, attempt):
        if attempt == self.code:
            return True
        else:
            return False

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

    def use_item(self, contents=[]):
        if self.item in contents:
            print(self.item.use_text)
            print()
            print(self.success_text)
            contents.remove(self.item)
            self.room.character = None
        else:
            print(self.hint)

class Twin(Character):
    def __init__(self, character_description, item, success_text, hint, pair=[None,None]):
        super().__init__(character_description, item, success_text, hint)
        self.pair = pair

    def use_item(self, contents=[]):
        for character in self.pair:
            if character.item in contents:
                print(character.item.use_text)
                print()
                print(character.success_text)
                contents.remove(self.item)
                self.room.character = (self.room.character - [self])[0]
            else:
                print("HINT: "+self.hint)        
    
class Trader(Character):
    def __init__(self, character_description, item, success_text, hint, held=None, next=None):
        super().__init__(character_description, item, success_text, hint)
        self.held_item = held
        self.next_trader = next

    def use_item(self, contents=[]):
        if self.item in contents:
            print(self.item.use_text)
            print()
            print(self.success_text)
            contents.remove(self.item)
            contents.append(self.held_item)
            self.room.character = self.next_trader
        else:
            print("HINT: "+self.hint)


class Item():
    def __init__(self, name, description, use_text):
        self.name = name
        self.description = description
        self.use_text = use_text

class Inventory():
    def __init__(self):
        self.contents = []

    def display(self):
        print()
        print("Inventory:")
        print("   ", end='')
        print('\n   '.join([item.name for item in self.contents]))
        print()