import math

class Layer:
    def __init__(self, index):
        self.index = index
        self.squares = []
        if index == 0:
            self.max_layer_size = 1
        else:
            self.max_layer_size = 8 * index

    def __repr__(self):
        return "index: {}, squares: {}".format(self.index, self.squares)

    def isFull(self):
        return len(self.squares) == self.max_layer_size

    def getEdge(self, edge):
        edge_of_layer = self.max_layer_size/4
        start = edge_of_layer * edge
        return self.squares[start : start + edge_of_layer]

    def addSquare(self, previous_layer=None):
        if previous_layer is None:
            self.squares.append(1)
        else:
            new_index = len(self.squares)
            edge_of_layer = self.max_layer_size/4 # how many squares are on each edge
            edge_number = new_index / edge_of_layer # should be 0 1 2 or 3
            index_in_edge = (new_index) % edge_of_layer # what is the index relative to the edge

            previous_layer_sum = 0
            previous_layer_size = previous_layer.max_layer_size
            if len(previous_layer.squares) == 1:
                previous_layer_sum = 1
            else:
                if new_index <= 1:
                    previous_layer_sum += previous_layer.squares[previous_layer_size-1]

                previous_edge = previous_layer.getEdge(edge_number)

                previous_indexes_to_add = [index_in_edge, index_in_edge - 1, index_in_edge - 2]
                for index in previous_indexes_to_add:
                    if index >= 0 and index <= len(previous_edge) - 1:
                        previous_layer_sum += previous_edge[index]

                if edge_number > 0 and index_in_edge <= 1:
                    previous_previous_edge = previous_layer.getEdge(edge_number - 1)
                    previous_layer_sum += previous_previous_edge[len(previous_previous_edge) - 1]

            current_layer_sum = 0
            if new_index != 0:
                current_layer_sum = self.squares[new_index - 1]

            if new_index + 1 > edge_of_layer:
                if index_in_edge == 0:
                    current_layer_sum += self.squares[new_index - 2]

            if new_index >= self.max_layer_size - 2:
                current_layer_sum += self.squares[0]

            value = previous_layer_sum + current_layer_sum

            self.squares.append(value)

            return value

class Memory:
    def __init__(self):
        self.layers = [Layer(0)]
    def __repr__(self):
        return "layers: {}".format(self.layers)
    def addSquare(self):
        for index, layer in enumerate(self.layers):
            if not layer.isFull():
                previous_layer = None
                if index != 0:
                    previous_layer = self.layers[index - 1]
                layer.addSquare(previous_layer)
                return
        # if we are full, add new layer
        previous_layer = self.layers[len(self.layers) - 1]
        layer = Layer(len(self.layers))
        self.layers.append(layer)
        return layer.addSquare(previous_layer)

memory = Memory()
while True:
    value = memory.addSquare()
    if value >= 361527:
        print "reached value {}".format(value)
        break
print memory
