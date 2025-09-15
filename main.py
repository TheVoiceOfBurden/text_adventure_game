from classes import Room, Item, Character

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

crowd = Character(
    "A horde of lost nooglers (new googlers) surrounds you and asks how to get around.  Type 'use' to give them your map to help them out.",
    map,
    "They gratefully accept the map.  Now that they know where to go they immediately leave. You, on the other hand, feel a bit lost.",
    "They will need something to help them get around.")
dog = Character(
    "A cute robot dog paces back and forth, clearly guarding a door.",
    banana,
    "The robot dog walks unknowingly towards the banana peel.  Its foot slips and its circuitry shuts down in response.  It lays on its side, happily wagging its robot tail.",
    "The floor seems to have a lot of traction."
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
    character="crowd"
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

entry.link(palm, "north")
palm.link(field, 'north')
field.link(park, 'north')
park.link(campus, 'west')
campus.link(vball, 'west')
campus.link(merc_entry, 'south')
merc_entry.link(jasmine, 'west')
cafe.link(jasmine, 'east')

current_room = entry
result = ""
while True:
    # Display map
    print(result)
    current_room.display_room()
    if current_room.item:
        current_room.display_item()
    elif current_room.character:
        current_room.display_character()
    current_room.display_exits()

    command = input("> ")
    if command in ['north', 'east', 'south', 'west', 'up', 'down']:
        current_room = current_room.move(command)
        



