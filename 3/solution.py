import math

def getLayer(number):
    '''Determines the layer number in the wheel that the given index is at. The center is 0, spots 1-9 are 1, and so on'''
    layer = 0;
    remainder = number - 1
    while remainder > 0:
        remainder -= ((layer + 1) * 8)
        layer += 1
    return layer

def getAllIndecesBeforeLayer(layer):
    if layer is 1:
        return 1
    return ((math.pow(layer - 1,2) + layer - 1)/2) * 8 + 1

def getIndexInFinalLayer(number):
    '''Returns the index in the residing layer of ram that this index occupies. Indexed at 0'''
    layer = getLayer(number);
    spotsInPreviousLayers = getAllIndecesBeforeLayer(layer)
    return number - spotsInPreviousLayers - 1

def getCardinalSpotsOfLayer(layer):
    '''Gets East, North, West, and South indeces in the final ring'''
    spotsInPreviousLayers = getAllIndecesBeforeLayer(layer)
    spotsInThisLayer = layer * 8
    quarter = spotsInThisLayer/4
    return [
        spotsInPreviousLayers + layer,
        spotsInPreviousLayers + layer + quarter,
        spotsInPreviousLayers + layer + quarter + quarter,
        spotsInPreviousLayers + layer + quarter + quarter + quarter,
    ]

# print(getAllIndecesBeforeLayer(1))
# print(getAllIndecesBeforeLayer(2))
# print(getAllIndecesBeforeLayer(3))
# print(getAllIndecesBeforeLayer(4))

index = 361527

layer = getLayer(index)
indexInFinalLayer = getIndexInFinalLayer(index)
cardinals = getCardinalSpotsOfLayer(layer)

closest = cardinals[0]
minDistance = math.fabs(index - closest)
for cardinal in cardinals:
    distance = math.fabs(index - cardinal)
    if distance < minDistance:
        minDistance = distance

print minDistance + layer