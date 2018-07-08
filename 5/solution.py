jumps = []

with open("/Users/conrad/Desktop/adventofcode2017/5/input.txt", "r") as f:
    for line in f:
        jumps.append(int(line))

index = 0

steps = 0

while index + 1 <= len(jumps):
    jump = jumps[index]

    if jump >= 3:
        jumps[index] = jump - 1
    else:
        jumps[index] = jump + 1

    index += jump
    steps += 1

print(steps)
