import re

class Node:
    def __init__(self, name=None, weight=None, children={}):
        self.name = name
        self.weight = weight
        self.children = children
        self.__total_weight = None

    def add(self, node):
        '''Attempt to add a node to this node or one of its descendants'''
        if node.name in self.children:
            self.children[node.name] = node
            return True
        else:
            for i in self.children:
                if self.children[i] is not None:
                    added = self.children[i].add(node)
                    if added:
                        return added
        return False

    def get_total_weight(self):
        '''gets total weight of this node plus all children nodes'''
        if self.__total_weight is not None:
            # if we already have a total weight calculated for this node, just return it
            return self.__total_weight
        self.__total_weight = self.weight
        for key, child in self.children.items():
            self.__total_weight += child.get_total_weight()
        return self.__total_weight

    def balance(self):
        '''attempt to find and fix the offending weight in this node's branches'''
        total_children = len(self.children)
        diffs = {}
        if total_children > 0:
            first_weight = None
            for key, child in self.children.items():

                # first balance this branch. if we find the balance issue in this branch,
                # return it to the top
                balance = child.balance()
                if balance is not None:
                    return balance

                this_child_weight = child.get_total_weight()

                if first_weight is None:
                    first_weight = this_child_weight
                    continue

                diff = this_child_weight - first_weight
                if diff != 0:
                    if len(diffs) == 1:
                        # if we get here, then the first child had the wrong weight
                        key = self.children.iterkeys().next()
                        return self.children[key].weight + diffs[key]
                    diffs[key] = diff

        if len(diffs) > 0:
            # we have found the bad weight, calculate new weight
            key = diffs.iterkeys().next()
            return self.children[key].weight - diffs[key]
        return None

        

# start with a placeholder root
ROOT = Node()

with open("/Users/conrad/Desktop/adventofcode2017/7/input.txt", "r") as f:
    for line in f:
        parts = re.split(",?\s", line)

        name = parts[0]
        if name == "ugml":
            x = 0
        weight = int(re.sub("[\(\)]", "", parts[1]))

        children = {}
        if len(parts) > 3:
            for i in range(3, len(parts)-1):
                children[parts[i]] = None

        NODE = Node(name=name, weight=weight, children=children)

        if len(children) > 0:
            for i in children:
                if i in ROOT.children:
                    NODE.add(ROOT.children[i])
                    del ROOT.children[i]

        if not ROOT.add(NODE):
            # track it as not having a parent yet
            ROOT.children[NODE.name] = NODE

print ROOT.balance()
