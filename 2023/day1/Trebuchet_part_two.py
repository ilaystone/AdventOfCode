#*********************************************************#
# ilay stone
#*********************************************************#

# imports
import re

# data definition
use_real_data = True
data_as_string = ''
if use_real_data:
    with open('real_input', 'r') as file:
        data_as_string = file.read()
else:
    data_as_string = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
data_arr = []
data_arr = data_as_string.strip().split('\n')

# functionality

def word_to_number(word):
    number_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    return number_mapping.get(word, word)

words_to_match = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def lookAheadRefineData(statement: str):
    res = ''
    for i, _ in enumerate(statement):
        new_statement = statement[i:len(statement)]
        for word in words_to_match:
            sub_str_to_match = new_statement[0:len(word)]
            if sub_str_to_match == word:
                res += word_to_number(word)
    
    return res

def resolveFirstLastNumbers(val):
    res = ''
    for char in val:
        if char.isdigit():
            res += char
            break;
    for char in reversed(val):
        if char.isdigit():
            res += char
            break;
    return res

total = 0

for statement in data_arr:
    total += int(resolveFirstLastNumbers(lookAheadRefineData(statement)))
    
print(total)
