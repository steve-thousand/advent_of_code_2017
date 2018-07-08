import math

rows = []

with open("/Users/conrad/Desktop/adventofcode2017/3/input.txt", "r") as f:
    for line in f:
        columns = line.split();
        for index, column in enumerate(columns):
            columns[index] = int(column)
        rows.append(columns);

def getDifferenceForRow(row):
    for column in row:
        for column2 in row:
            if column > column2 and column % column2 is 0:
                return column / column2

checksum = 0
for i in rows:
    checksum += getDifferenceForRow(i)
        
print(checksum)