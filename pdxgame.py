import random

# Basic class for user-created player.

class Player():
    def __init__(self, name):
        self.hp = 90
        self.name = name
    def increase_hp(self, hp):
        self.hp += hp
    def decrease_hp(self, hp):
        self.hp -= hp

# Different types of players user can choose.

class Hipster(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(20, 50)

class Panhandler(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(5, 15)

class Vegan(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(15, 30)

class BeardedTechie(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(5, 50)

# Tiles for the player's location.

class Tile():
    def __init__(self, exits):
        self.exits = exits

# Method to move to different tiles in the game.

def tile_change(tile):
    tiles = ''
    for x in tile.exits.keys():
        tiles += x + ' '
    try:
        tile_choice = raw_input("What direction do you choose? %s ? > " % tiles)
        play(tile.exits[tile_choice])
    except KeyError:
        print "I do not understand that."
        tile_change(tile)

# Creates random outcomes for the player in a new tile.

def randomizer(player):

    response = [ "Rain", "Canvasser", "Naked Bike Ride", "Bike Messengers", "Rush Hour",
                 "Free Box", "Freak Sunshine", "Coffee and Donuts", "Thrift Store Find",
                 "Free Hugs"]
    response_num = random.randint(0,9)
    if response_num > 4:
        player.increase_hp(10)
    else:
        player.decrease_hp(10)
    print "You have %s hipster points." % player.hp
    return response[response_num]

def choose_player():
    player_type = raw_input(""" What type of Portlander are you? Choose:
                                0 for hipster
                                1 for vegan
                                2 for panhandler
                                3 for bearded techie """)
    player_name = raw_input("And what do you like to be called?")
    return player_type, player_name

def move(tile, player):
    print "You are in Portland."
    obstacle = randomizer(player)
    print obstacle
    tile_change(tile)

player_type, player_name = choose_player()

if player_type == "0":
    player = Hipster(player_name)

elif player_type == "1":
    player = Vegan(player_name)

elif player_type == "2":
    player = Panhandler(player_name)

elif player_type == "3":
    player = BeardedTechie(player_name)

else:
    print "Sorry, there are no other options."

tile1 = Tile( {} )
tile2 = Tile( {} )
tile1.exits = {"Forward": tile2}
tile2.exits = {"Back": tile1}
move(tile1, player)
