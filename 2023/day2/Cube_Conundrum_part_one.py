#*********************************************************#
# ilay stone
#*********************************************************#

from collections import defaultdict
import re

# data definition
use_real_data = True
data_as_string = ''
if use_real_data:
    with open('real_input', 'r') as file:
        data_as_string = file.read()
else:
    data_as_string = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def calculateTotal(sequence):
    pattern = re.compile(r'(\d+) (\w+)')
    color_counts = defaultdict(list)
    matches = pattern.findall(sequence)
    
    for count, color in matches:
        count = int(count)
        color_counts[color].append(count)
        
    values_dict = dict(color_counts)
    
    return values_dict

red = 12
blue = 14
green = 13

def checkPossible(sequenceDict):
    for val in sequenceDict['red']:
        if val > red:
            return False
    for val in sequenceDict['blue']:
        if val > blue:
            return False
    for val in sequenceDict['green']:
        if val > green:
            return False
    return True

possible_games = 0
id = 1

for game in data_as_string.strip().split('\n'):
    if (checkPossible(calculateTotal(game))):
        possible_games += id
    id += 1
        
print(possible_games)