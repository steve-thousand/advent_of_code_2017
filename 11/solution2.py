import math

class Movement:
    def __init__(self, north, direction=0):
        self.north = north
        self.direction = direction
        self.nextMovement = None

    def pushNextMovement(self, nextMovement):
        self.nextMovement = nextMovement

    def hasNextMovement(self):
        return self.nextMovement is not None

    def getNextMovement(self):
        return self.nextMovement

    def canReplace(self, potentialMovement):
        if self.north == potentialMovement.north:
            # same north but opposite directions?
            if math.fabs(self.direction - potentialMovement.direction) == 2:
                # combine example nw and ne to be n
                return Movement(self.north)
        elif self.direction == -potentialMovement.direction:
            # these are opposites! CANCEL >:(
            return None
        elif math.fabs(self.direction - potentialMovement.direction) == 1:
            # we have gone some non-zero direction, and then a zero direction. replace with direction in opposite north
            if potentialMovement.direction == 0:
                return Movement(potentialMovement.north, self.direction)
            else:
                return Movement(self.north, potentialMovement.direction)
        # -1 means can't replace
        return -1

def N():
    return Movement(1)
def NE():
    return Movement(1, 1)
def SE():
    return Movement(0, 1)
def S():
    return Movement(0)
def SW():
    return Movement(0, -1)
def NW():
    return Movement(1, -1)

MOVEMENTS_BY_DIRECTION = {
    'n'  : N,
    'ne' : NE,
    'se' : SE,
    's'  : S,
    'sw' : SW,
    'nw' : NW
}

DIRECTIONS = []

with open("/Users/conrad/Desktop/adventofcode2017/11/input.txt", "r") as f:
    DIRECTIONS = list(f.read().split(","))

# root is an empty north, ignore it later
rootMovement = Movement(1) 

def addMovement(movementToAdd):
    # walk through the movements, see if we find one we can replace, else append
    previousMovement = None
    currentMovement = rootMovement
    replaced = False
    while currentMovement.hasNextMovement():
        previousMovement = currentMovement
        currentMovement = currentMovement.nextMovement
        canReplaceMovement = currentMovement.canReplace(thisMovement)
        if canReplaceMovement != -1:
            replaced = True
            previousMovement.pushNextMovement(currentMovement.getNextMovement())
            if canReplaceMovement is not None:
                addMovement(canReplaceMovement)
            break
        
    if not replaced:
        currentMovement.pushNextMovement(thisMovement)

for direction in DIRECTIONS:

    if direction == 'n':
        x = 0

    thisMovement = MOVEMENTS_BY_DIRECTION[direction]()

    addMovement(thisMovement)

steps = 0
currentMovement = rootMovement
while currentMovement.hasNextMovement():
    currentMovement = currentMovement.getNextMovement()
    steps += 1

print steps