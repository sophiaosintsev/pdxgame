import random

# Basic class for user-created player.

class Player():
    def __init__(self, name):
        self.hp = 90 + random.randint(5, 15)
        self.name = name
    def increase_hp(self, hp):
        self.hp += hp
    def decrease_hp(self, hp):
        self.hp -= hp

# Different types of players user can choose.

# class Hipster(Player):
#
# class Panhandler(Player):
#
# class Vegan(Player):
#
# class BeardedTechie(Player):

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

# Random outcomes for the player in a new tile.

def randomizer():

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

def play(tile):
    print "You are in Portland."
    obstacle = randomizer()
    print obstacle
    tile_change(tile)

name = raw_input("Name your player. ")
player = Player(name)
tile1 = Tile( {} )
tile2 = Tile( {} )
tile1.exits = {"Forward": tile2}
tile2.exits = {"Back": tile1}
play(tile1)
