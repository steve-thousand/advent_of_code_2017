import re

with open("/Users/conrad/Desktop/adventofcode2017/6/input.txt", "r") as f:
    content = f.read()
    array = re.compile("\s+").split(content)
    for index, i in enumerate(array):
        array[index] = int(i)

def reallocate(array_to_reallocate):
    '''Walk through the array once and reallocate blocks'''

    # walk array and find the max value and its index
    highest_index = 0
    max_blocks = 0
    for index, i in enumerate(array_to_reallocate):
        if i > max_blocks:
            max_blocks = i
            highest_index = index 
        
    # we should now have the highest number and its index

    # wipe orginal
    array_to_reallocate[highest_index] = 0

    # walk through array, adding
    for i in range(max_blocks):
        highest_index += 1
        if highest_index > len(array_to_reallocate) - 1:
            highest_index = 0
        array_to_reallocate[highest_index] = array_to_reallocate[highest_index] + 1

    return array_to_reallocate

STATES = {}

steps = 0
while True:
    array = reallocate(array);
    steps += 1
    string = "".join(str(x) for x in array);
    if string in STATES:
        break
    STATES[string] = steps

print(steps - STATES[string])