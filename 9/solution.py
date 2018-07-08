with open("/Users/conrad/Desktop/adventofcode2017/9/input.txt", "r") as f:
    INPUT_STREAM = f.read()

TOTAL_GROUPS = 0
SCORE = 0

OPEN_GROUPS = 0
NEGATED = False
GARBAGE_ESCAPED = False
TOTAL_GARBAGE = 0
for i in INPUT_STREAM:
    if not NEGATED and i == '!':
        NEGATED = True
    elif not GARBAGE_ESCAPED and i == '<':
        GARBAGE_ESCAPED = True
    else:
        if NEGATED:
            NEGATED = False
            continue
        if GARBAGE_ESCAPED:
            if i == '>':
                GARBAGE_ESCAPED = False
            else:
                TOTAL_GARBAGE += 1
            continue
        if i == '{':
            OPEN_GROUPS += 1
        elif i == '}':
            SCORE += OPEN_GROUPS
            OPEN_GROUPS -= 1
            TOTAL_GROUPS += 1

print TOTAL_GROUPS
print SCORE
print TOTAL_GARBAGE
