LENGTHS = []

with open("/Users/conrad/Desktop/adventofcode2017/10/input.txt", "r") as f:
    PARTS = list(f.readline())
    for i in PARTS:
        LENGTHS.append(ord(i))

LENGTHS.extend([17, 31, 73, 47, 23])

print LENGTHS

STRING = range(256)
TOTAL_LENGTH = len(STRING)

POSITION = 0
SKIP_SIZE = 0

for i in range(64):
    x = 0
    for length in LENGTHS:
        virtual_start = POSITION
        virtual_end = virtual_start + length - 1
        while virtual_end > virtual_start:
            actual_start = virtual_start % TOTAL_LENGTH
            actual_end = virtual_end % TOTAL_LENGTH
            first = STRING[actual_start]
            STRING[actual_start] = STRING[actual_end]
            STRING[actual_end] = first
            virtual_end -= 1
            virtual_start += 1
        POSITION += length + SKIP_SIZE
        SKIP_SIZE += 1

print POSITION
print SKIP_SIZE

hash = ""
for i in range(16):
    value = STRING[16 * i]
    for j in range(1, 16):
        value = value ^ STRING[(16 * i) + j]
    this_hex = hex(value)[2:]
    while len(this_hex) < 2:
        this_hex = "0" + this_hex
    hash += this_hex

print hash