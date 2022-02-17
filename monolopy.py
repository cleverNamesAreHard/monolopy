from random import randint
from time import time
import os


# I felt this would be the easiest way to store both:
#   the lookup value (name), and the data (count)
class Tile:
    # Create the Tile object from the name, given by the user
    def __init__(self, name):
        self.name = name
        self.count = 0

    # Just a pretty, programmatic way to set the value.
    def set_count(self, new_count):
        self.count = new_count

# Makes it easy to reference where the player is (position variable)
#  against what tile they're on (to lookup, and increment count)
board = {
    0: "Go",
    1: "Mediterranean Avenue",
    2: "Community Chest",
    3: "Baltic Avenue",
    4: "Income Tax",
    5: "Reading Railroad",
    6: "Oriental Avenue",
    7: "Chance",
    8: "Vermont Avenue",
    9: "Connecticut Avenue",
    10: "Jail / Just Visiting",
    11: "St. Charles Place",
    12: "Electric Company",
    13: "States Avenue",
    14: "Virginia Avenue",
    15: "Pennsylvania Railroad",
    16: "St. James Place",
    17: "Community Chest",
    18: "Tennessee Avenue",
    19: "New York Avenue",
    20: "Free Parking",
    21: "Kentucky Avenue",
    22: "Chance",
    23: "Indiana Avenue",
    24: "Illinois Avenue",
    25: "B. & O. Railroad",
    26: "Atlantic Avenue",
    27: "Ventnor Avenue",
    28: "Water Works",
    29: "Marvin Gardens",
    30: "Go To Jail",
    31: "Pacific Avenue",
    32: "North Carolina Avenue",
    33: "Community Chest",
    34: "Pennsylvania Avenue",
    35: "Short Line",
    36: "Chance",
    37: "Park Place",
    38: "Luxury Tax",
    39: "Boardwalk"
}

# ANSI Escape Sequences, used to make it pretty-print in color.
colors = {
    "blue": "\033[34m",
    "green": "\033[32m",
    "red": "\033[31m",
    "white": "\033[97m",
}

# These will be pretty-printed differently.
discludes = ["Chance", "Community Chest"]

# This will enable ANSI Escape Chars in terminal.
os.system("")

# This is the only variable you should be changing.
# This is the number of times around the board, not the number of turns.
size_of_test = 500000
# These are storage or variables for the below logic
full_loops = 0
position = 0
results = []
total_tiles = 0
start_time = time()

while full_loops < size_of_test:
    # Extract Tile object names from the existing list.
    # Tiles are stored in list 'results' for lookup later.
    tile_names = [tile.name for tile in results]
    # This is where the stats people are gonna roast me.
    dice_roll = randint(1, 6)
    # If you've gone above position 39 (see line 57), you'll pass Go
    #   and also will have to reset your position, and add a full loop.
    if position + dice_roll >= 39:
        position = (position + dice_roll) % 39
        full_loops += 1
    else:
        position = position + dice_roll

    tile_name = board[position]
    # The easy way
    if tile_name not in tile_names:
        tile = Tile(tile_name)
        results.append(tile)
    # The hard way
    else:
        # If this could be done without a loop, the program would be much
        #   more efficient.  Until then:
        # This is how I'm looking up the right tile object in 'results'
        tile = next(
            (tile_ for tile_ in results if tile_.name == tile_name), 
            None
        )
        # Increment the data, with a safety check
        if tile is not None:
            tile.set_count(tile.count + 1)
    # This lets us calculate a percentage of tile landings.
    total_tiles += 1

# Sorting ascending to get bottom ten, and sorting descending for top ten
#   and pretty-print
results.sort(key=lambda tile: tile.count, reverse=False)
bottom_ten = [tile.name for tile in results[0:10]]
results.sort(key=lambda tile: tile.count, reverse=True)
# Chance and Community Chest will be the top by more than 5% in a large
#   sample size.
top_ten = [tile.name for tile in results[2:12]]

# Just for statistics sake
end_time = time()

# Table headers
print("\n{:<24}| %% Tiles".format("Tile Name"))
# Bar between headers and first row.
print("{}|{}".format("-" * 24, "-" * 10))
for tile in results:
    # Determine what color to print the line as, defaulting to white
    color = colors["white"]
    if tile.name in top_ten:
        color = colors["green"]
    elif tile.name in bottom_ten:
        color = colors["red"]
    elif tile.name in discludes:
        color = colors["blue"]
    # Pretty-Print
    print(color, "{:<24}| {:.4%}".format(
        tile.name,
        tile.count / total_tiles
    ))

# Revert back to standard color, or the terminal will remain red.
color = colors["white"]
# Moar data
print(color, "\nEllapsed Time: {:.2f} seconds".format(
    end_time - start_time
))
