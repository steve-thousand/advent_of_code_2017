import math;

DIRECTIONS = []

with open("/Users/conrad/Desktop/adventofcode2017/11/input.txt", "r") as f:
    DIRECTIONS = list(f.read().split(","))

MOVES_PER_DIRECTION = [
    0,
    0,
    0,
    0,
    0,
    0
]

INDEX_OF_DIRECTION = {
    'nw': 0,
    'n' : 1,
    'ne': 2,
    'se': 3,
    's' : 4,
    'sw': 5,
}

for direction in DIRECTIONS:
    index = INDEX_OF_DIRECTION[direction]
    if index < 3:
        NORTH = True
    else:
        NORTH = False
    MOVES_PER_DIRECTION[index] += 1 if NORTH else -1

for direction in range(3):
    moves = MOVES_PER_DIRECTION[direction]
    opposite_direction = (direction + 3) % 6
    if MOVES_PER_DIRECTION != 0:
        MOVES_PER_DIRECTION[direction] -= moves
        MOVES_PER_DIRECTION[opposite_direction] += moves

print MOVES_PER_DIRECTION

# cancel out west and easts
if MOVES_PER_DIRECTION[0] > 0 and MOVES_PER_DIRECTION[2] > 0:
    move_west = MOVES_PER_DIRECTION[0]
    MOVES_PER_DIRECTION[0] = 0
    diff = MOVES_PER_DIRECTION[2] - move_west
    if diff >= 0:
        MOVES_PER_DIRECTION[2] = diff
    else:
        MOVES_PER_DIRECTION[2] = 0
        MOVES_PER_DIRECTION[0] = -diff
    MOVES_PER_DIRECTION[1] += move_west - diff
if MOVES_PER_DIRECTION[5] < 0 and MOVES_PER_DIRECTION[3] < 0:
    move_west = MOVES_PER_DIRECTION[5]
    MOVES_PER_DIRECTION[5] = 0
    diff = MOVES_PER_DIRECTION[3] - move_west
    if diff <= 0:
        MOVES_PER_DIRECTION[3] = diff
    else:
        MOVES_PER_DIRECTION[3] = 0
        MOVES_PER_DIRECTION[5] = -diff
    MOVES_PER_DIRECTION[4] -= move_west + diff

print MOVES_PER_DIRECTION

total = 0
for moves in MOVES_PER_DIRECTION:
    total += math.fabs(moves)

print total