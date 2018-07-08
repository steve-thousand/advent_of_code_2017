REGISTERS = {}
HIGHEST_VALUE = 0

OPERATORS = {
    ">": lambda x,y: x > y,
    "<": lambda x,y: x < y,
    ">=": lambda x,y: x >= y,
    "<=": lambda x,y: x <= y,
    "==": lambda x,y: x == y,
    "!=": lambda x,y: x != y
}

class Instruction:
    def __init__(self, register, increase, delta, condition_register, operand, compare):
        self.register = register
        self.increase = increase
        self.delta = delta
        self.condition_register = condition_register
        self.operand = operand
        self.compare = compare

    def execute(self):
        if self.condition_register in REGISTERS:
            comparing = REGISTERS[self.condition_register]
        else:
            comparing = 0

        operator_lambda = OPERATORS[self.operand]
        if operator_lambda(comparing,self.compare):
            if self.register in REGISTERS:
                value = REGISTERS[self.register]
            else:
                value = 0
            if self.increase:
                value += self.delta
            else:
                value -= self.delta
            REGISTERS[self.register] = value
            return value

with open("/Users/conrad/Desktop/adventofcode2017/8/input.txt", "r") as f:
    for line in f:
        parts = line.split(" ")
        instruction = Instruction(
            parts[0],
            parts[1] == "inc",
            int(parts[2]),
            parts[4],
            parts[5],
            int(parts[6])
        )
        value = instruction.execute()
        if value is not None and value > HIGHEST_VALUE:
            HIGHEST_VALUE = value

maxValue = None
for key, value in REGISTERS.items():
    if maxValue is None or value > maxValue:
        maxValue = value

print HIGHEST_VALUE