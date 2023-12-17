#*********************************************************#
# ilay stone
#*********************************************************#

# data definition
use_real_data = True
data_as_string = ''
if use_real_data:
    with open('real_input', 'r') as file:
        data_as_string = file.read()
else:
    data_as_string = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
data_arr = []
data_arr = data_as_string.strip().split('\n')

#function definition

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


result = 0
for val in data_arr:
    result += int(resolveFirstLastNumbers(val))

print(result)

