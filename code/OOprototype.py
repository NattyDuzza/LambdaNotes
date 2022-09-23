import pydot as pd

graph = pd.Dot(graph_type="graph", rankdir="UD")

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
    def __init__(self, nodes, names):
        self._nodes = nodes
        self._names = names

    def edges(self):
        for i in range(0, len(self._names)):
            parent = self._nodes[self._names[i]].name()
            for j in range(0, len(self._nodes[self._names[i]].connections)):
                edge = pd.Edge(parent, self._nodes[self._names[i]].connections[j])
                graph.add_edge(edge)



nodes = {}
names = [] # not very happy with using this structure, seems clunky but was a quick fix to a mistake I had made

count = 0
lastNode = 0
firstNode = True

while count < 15:
    
    if lastNode != 0:
        currentIndex = names.index(lastNode)
    
    nextInput = input("Enter: ")
    
    if nextInput == "<":
        lastNode = names[currentIndex - 1]
    
    else:

        if nextInput not in nodes:
            nodes[nextInput] = Node(nextInput)
            names.append(nextInput)

        if firstNode != True:
            nodes[nextInput].connector(lastNode)
            lastNode = nodes[nextInput].name()
        else:
            firstNode = False
            lastNode = nextInput

    count += 1

#print(nodes)

#print(nodes['a'].connections)  

map1 = MindMap(nodes, names)
map1.edges()

graph.write_png("/tmp/test.png")
