from classes import Room, Lockbox, Item, Character, Inventory, Trader
import os
#TODO Implement, Add Friends, Finish Lockbox, change wrap text length

map = Item(
    "map",
    "You see a map on a bench.  Type 'grab' to pick it up.",
    "You give the map to the horde of nooglers."
    )
banana = Item(
    "peel",
    "You find a banana peel next to the compost bin.  Clearly someone needs to work on their basketball skills.",
    "You strategically drop the banana peel on the robot dog's path."
    )
swatter = Item(
    "fly swatter",
    "You notice a fly swatter on someone's desk.",
    "You smack the monitor with the fly swatter."
)
croc = Item(
    "costume",
    "Laying in the middle of the path is a crocodile costume.",
    'You put on the crocodile costume and say, "See you later alligator."'
)
sword = Item(
    "I'm Feeling Lucky sword",
    "A ray of light reflects off a shiny metal object.  You realize you have found the I'm Feeling Lucky sword.",
    "You strike Precision with the I'm Feeling Lucky sword."
)
shield = Item(
    "Sheild of Android",
    "The Shield of Android hangs on a wall.",
    "You bash recall with the Shield of Android."
)
stickers = Item(
    "assortment of doodle stickers",
    "You find a bowl full of doodle stickers with a warning to take just one or two.",
    "You ask to trade for your doodle stickers."
)
banana_whole = Item(
    'banana',
    '',
    "You ask to trade for your banana."
)
quinoa = Item(
    'cup of quinoa',
    "",
    "You ask to trade for your quinoa."
)
diet_soda = Item(
    'can of diet soda',
    "",
    "You ask to trade for your diet soda."
)
latte = Item(
    'latte',
    "",
    "You ask to trade for your latte."
)
sticky = Item(
    'sticky note with some clues of it',
    '',
    '''You read your sticky note with the clues:
1. I am the beginning of everything, the end of everywhere. I'm the beginning of eternity, the end of time & space. What am I?
2. I am the loneliest number.
3. Check the clue number.
4. Take a number. Double it. Add 21. Subtract 15. Divide by 2. Subtract your original number.
5. To make this number even, you take the s out.'''
)

crowd = Character(
    "A horde of lost nooglers (new googlers) surrounds you and asks how to get around.  Type 'use' to give them your map to help them out.",
    map,
    "They gratefully accept the map.  Now that they know where to go they immediately leave. You, on the other hand, feel a bit lost.",
    "They will need something to help them get around."
    )
dog = Character(
    "A cute robot dog paces back and forth, clearly guarding a door.",
    banana,
    "The robot dog walks unknowingly towards the banana peel.  Its foot slips and its circuitry shuts down in response.  It lays on its side, happily wagging its robot tail.",
    "The floor seems to have a lot of traction."
    )
alligator = Character(
    "An alligator blocks the building to the north.",
    croc,
    'The alligator looks up at you and replies, "after a while crocodile" and walks away.',
    "A rhyme about alligators leaving."
)
recall = Character(
    "A sad, grieving spirit of Recall still blocks your way as it mourns its twin.",
    shield,
    "The broad side of the shield manages to hit most of the ghoul.  Its screeches in pain and vanishes before your eyes.",
    "I need something that will cover all of recall."
)
ghouls = Trader(
    "You are greeted by the ferocious twin ghouls of Precision and Recall.",
    sword,
    "The sword strikes Precision and the magical incantation for luck bursts like a grenade of light through the ghoul.  Its twin laughs at your precise but harmless cuts.  Clearly you'll need another way of going after Recall.",
    "I might need something sharp and to the point.",
    None,
    recall
)
engineer = Character(
    "You find a frustrated ground of engineers trying to solve a bug.",
    swatter,
    "The screen shows static for a second and reverts back. The distraction allows an engineer to see something they didn't before. They fix the bug and answer your question about your missing buddy.",
    "Find something used for eliminating bugs"
)
caffinated = Trader(
    "You land on a over caffeinated googler with a glass of water.",
    latte,
    '''The over caffeinated googler gladly accepts your latte. "Thank you for the latte, I hear you are looking for your friend.  I'll only tell you this once."

1. I am the beginning of everything, the end of everywhere. I'm the beginning of eternity, the end of time and space. What am I?
2. I am the loneliest number.
3. Check the clue number.
4. Take a number. Double it. Add 21. Subtract 15. Divide by 2. Subtract your original number.
5. To make this number even, you take the s out.''',
    "",
    sticky,
    None
)
grump = Trader(
    "You land on a over caffeinated googler with a glass of water and a grumpy engineer holding a latte.",
    diet_soda,
    '"You found the last one!", the grumpy engineer no longer looks so frustrated and puts down the latte with a beautiful flower made out of foam for the diet soda.',
    "",
    latte,
    caffinated
)
vp = Trader(
    "You land on a over caffeinated googler with a glass of water, a grumpy engineer holding a latte, and the vice president of some product you don't recognize with a diet coke in her hands.",
    quinoa,
    "You suggest water and quinoa to the VP.  Her eyes clearly show you've taken away a moment of respite, but the truth of your statement convinces her to give up the diet soda.",
    "",
    diet_soda,
    grump
)
noogler = Trader(
    "You land on a over caffeinated googler with a glass of water, a grumpy engineer holding a latte, the vice president of some product you don't recognize with a diet coke in her hands, and a happy noogler amazed that the micro-kitchen even offers quinoa.",
    banana_whole,
    "The noogler admits he doesn't even know what quinoa is and gratefully accepts your banana.",
    "",
    quinoa,
    vp
)
intern = Trader(
    "You land on a over caffeinated googler with a glass of water, a grumpy engineer holding a latte, the vice president of some product you don't recognize with a diet coke in her hands, a happy noogler amazed that the micro-kitchen even offers quinoa, and an excited intern holding a banana.",
    stickers,
    "The intern is so excited about the stickers she immediately gives you her banana.  You wonder what you can trade for this?",
    "You need something to trade.",
    banana_whole,
    noogler
)

entry = Room(
    "You see a statue of a metal man peeking out of a building.  A park is just across the street."
)
palm = Room(
    "A sidewalk circles around a palm tree.",
    item=map
)
field = Room(
    "You see a large field with googlers playing ultimate frisbee and dodgeball.",
    character = crowd
)
park = Room(
    "A park opens up all around you with a small waterfall showing you a path west towards the campus.",
    locked = [True, crowd, "The mass of nooglers blocks you from moving along your way."]
)
campus = Room(
    "The Google campus opens up before you.  Colorful lawn chairs greet your passage, and a building on your left hosts an image of your likeness and all of your friends."
)
vball = Room(
    "A T-rex skeleton towers over you and a beach volleyball court invites you to play."
)
merc_entry = Room(
    "You are inside the Mercury building.  You spot a micro-kitchen and some open cubicles.",
    item=banana
)
jasmine = Room(
    "You are greeted by a giant wall of jasmine.",
    character = dog
)
cafe = Room(
    "You enter the Messenger cafe, the smell of sandwiches and popcorn in the air.",
    locked=[True, dog, "So small and cute, the robot dog jumps at your lap blocking your way."]
)
p_lot = Room(
    "Two buildings hug the giant walkway and open up into a parking lot.",
    character = alligator
)
game_room = Room(
    "You find a small game room.",
    item=swatter
)
bridge = Room(
    "A bridge hovers over a shallow creek.  A cute duck quacks at you."
)
walkway = Room(
    "Palm trees and corporate art occupy the concrete walkway between the 3 buildings.",
    item=croc
)
venus_entry = Room(
    "You make your way into the Venus building.",
    locked=[True, alligator, 'The alligator says "Whoa, hold on friend. I can\'t let you in!"']
)
venus_gym = Room(
    "A bridge allows you to cross from building to building.  You see a gym lined with treadmills and weights."
)
venus_cafe = Room(
    "You've entered the Morning Star Cafe.  A flurry of food choices inundates your senses and ability to make a choice.",
    character=None
)
mars_lobby = Room(
    "You enter the lobby of the Mars building and above you a slide slithers its way to your side."
)
mars2 = Room(
    "You are on the 2nd floor.  Exiting the elevator, you see the top of the slide.  The temptation to ride it is very strong.",
    item=sword
)
mars3 = Room(
    "You are on the 3rd floor of the Mars building.  A graveyard of broken lava lamps sits in the middle of the floor.  A skybridge connects you to the other buildings."
)
strange = Room(
    "You find a strange hallway with clean rooms and signs with drawings of hazmat suits on them."
)
saturn2 = Room(
    "The 2nd floor of the Saturn building."
)
saturn3 = Room(
    "You are on the 3rd floor of the Saturn building.  You see a table with various jigsaw puzzles half finished.  A skybridge connects you to a different building."
)
saturn4 = Room(
    "You are on the 4th floor.  A mural of a violent green wave in the ocean greets your entrance.",
    character=ghouls
)
river1 = Room(
    "On your left you see a fake river comprised of rocks and on your right a piano. In fact, everything looks inviting except the elevators."
)
river2 = Room(
    "You are on the 2nd floor.  Cubicles as far as the eye can see."
)
river3 = Room(
    "You are on the 3rd floor.  You see a small micro-kitchen and a skybridge that will connect you to another building."
)
river4 = Room(
    "You are on the 4th floor.  An empty room with a giant whale, whose belly serves as a couch, greets you.",
    item=shield
)
whiteboard = Room(
    "You find a whiteboard filled with cartoonish drawings.",
    item=stickers
)
hallway_end = Room(
    "This is what you call the end of the hallway.",
    character=None
)
beach_V_ball = Room(
    "A beach volleyball court with a small sand castle in the middle grabs your attention."
)
busy_street = Room(
    "You come upon a busy street full of self-driving cars zooming past you."
)
building_entry = Room(
    "You enter a building to find a yet another gym on your right."
)
cubicles = Room(
    "You see a sea of cubicles.",
    character=engineer
)
massage = Room(
    "You find the massage room.",
    character = None,
    locked=[True, engineer, "The frustrated engineer waves you away like an annoying fly."]
)
cafeteria = Room(
    "You enter a small cafeteria.  People are standing around but no one is talking.",
    character=intern
)
lockbox = Lockbox(
    "You come upon a giant lockbox with an alphanumeric keypad which could easily fit a missing letter.",
    code="e1337"
)

entry.link(palm, 'north')
palm.link(field, 'north')
field.link(park, 'north')
park.link(campus, 'west')
campus.link(vball, 'west')
campus.link(merc_entry, 'south')
merc_entry.link(jasmine, 'west')
cafe.link(jasmine, 'east')
p_lot.link(vball, 'east')
venus_entry.link(p_lot, 'south')
venus_gym.link(venus_entry, 'west')
venus_cafe.link(venus_gym, 'west')
game_room.link(p_lot, 'north')
bridge.link(p_lot,'east')
walkway.link(bridge, 'east')
mars_lobby.link(walkway, 'south')
mars2.link(mars_lobby, 'up')
mars3.link(saturn3, 'west')
mars3.link(mars2, 'up')
river3.link(mars3, 'north')
river4.link(river3, 'down')
river2.link(river3, 'up')
river1.link(river2, 'up')
river1.link(walkway, 'north')
strange.link(walkway, 'east')
saturn2.link(strange, 'up')
saturn3.link(saturn2, 'down')
saturn4.link(saturn3, 'down')
whiteboard.link(saturn4, 'east')
hallway_end.link(whiteboard, 'east')
beach_V_ball.link(strange, 'east')
busy_street.link(beach_V_ball, 'north')
building_entry.link(busy_street, 'north')
cubicles.link(building_entry, 'east')
massage.link(cubicles, 'east')
cafeteria.link(building_entry, 'north')
lockbox.link(cafeteria, 'north')


short = {
    'n': 'north',
    'e': 'east',
    's': 'south',
    'w': 'west',
    'u': 'use',
    'p': 'up',
    'd': 'down',
    'g': 'grab',
    'i': 'inventory',
    'h': 'help',
    'x': 'exits',
    'm': 'map',
    'f': 'friends'
}

commands = '(n)orth, (s)outh, (e)ast, (w)est, u(p), (d)own, (g)rab, (i)nventory, (u)se, (h)elp, e(x)its, (m)ap, (f)riends'.split(', ')
current_room = entry

result ="""Type single word commands, no need to describe the subject.  For example,
'grab banana peel' should just be 'grab' or 'use banana peel' should just be 'use'

A strange tingle trickles across your skin.  You feel lightheaded and sit
down.  Feeling better you stand up again and notice your reflection in
a window.  You are still the same big blue G you've always been and you
can't help but smile.

But wait!  Where are your friends red o, yellow o, blue g, green l, and
the always quirky red e?
"""

inventory = Inventory()
friends = {
    'red o': False,
    'yellow o': False,
    'blue g': False,
    'green l': False,
    'red e': False
}
print(result)
current_room.display_room()
current_room.display_exits()


while True:
    # Display map
    command = input("> ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if command in short:
        command = short[command]
    if command in ['north', 'east', 'south', 'west', 'up', 'down']:
        current_room, result = current_room.move(command)
        print('\n' + result)
        current_room.display_room()
        current_room.display_exits()
    elif command == 'grab':
        if current_room.item:
            inventory.contents.append(current_room.item)
            print(f'{current_room.item.name} is added to your inventory!')
            current_room.item = None
            inventory.display()
        else:
            inventory.display()
    elif command == 'use':
        if current_room.character:
            current_room.character.use_item(inventory.contents)
            current_room.display_exits()
    elif command == 'exits':
        current_room.display_exits()            
    else:
        print(f"{command} isn't defined")
