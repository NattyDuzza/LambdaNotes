class Node:
    def __init__(self, name):
        self._name = name
        self.connections = []

    def name(self):
        return self._name

    def connector(self, previousNode):
        self.connections.append(previousNode)
        print(self.connections)


class MindMap:
    def __init__(self, nodes):
        self._nodes = nodes

    def edges(self):
        pass

nodes = {}
count = 0
lastNode = 0
firstNode = True

while count < 5:
    
    nextInput = input("Enter: ")
    if nextInput not in nodes:
        nodes[nextInput] = Node(nextInput)
    count += 1
    if firstNode != True:
        nodes[nextInput].connector(lastNode)
        lastNode = nodes[nextInput].name()
    else:
        firstNode = False
        lastNode = nextInput

print(nodes)

print(nodes['a'].connections)        

