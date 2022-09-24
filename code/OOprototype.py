import pydot as pd #imports package needed for mindmap output

graph = pd.Dot(graph_type="graph", rankdir="UD") #creates instance of graph, edges and nodes will be added 'into' this.

#Class Node is the class that will be a blueprint for every 'node' of data on the mind map. 
class Node: 
    def __init__(self, name):
        self._name = name 
        self.connections = [] #this is where the connected nodes to each instance will be stored.

    def name(self): #makes it easier to access the name of each object.
        return self._name 

    def connector(self, previousNode): 
        self.connections.append(previousNode) #adds the previous node (hence the node the instance which is using this function was connected onto) to the connections list
        print(self.connections) #simply for keeping track whilst prototyping.

#Class MindMap is a class that will handle the initialisation of a new mindmap and contructs it once all the nodes have been added. Not much use for now since we are only creating one mindmap but will be helpful when we move to full development.
class MindMap:
    def __init__(self, nodes, names):
        self._nodes = nodes
        self._names = names

    def edges(self):
        for i in range(0, len(self._names)): #iterates through the length of the list of node names (not happy with doing it this way)
            parent = self._nodes[self._names[i]].name() #sets the parent of the connection to the node with the name at the index i. Hence all nodes will be iterated over in this way.
            for j in range(0, len(self._nodes[self._names[i]].connections)): #iterates over the list of connections to the parent node
                edge = pd.Edge(parent, self._nodes[self._names[i]].connections[j]) #creates edge between parent and current node (at index j in the nodes connection list)
                graph.add_edge(edge) #adds edge to graph



nodes = {}
names = [] # not very happy with using this structure, seems clunky but was a quick fix to a mistake I had made

count = 0
lastNode = 0
firstNode = True


while True:
    
    if lastNode != 0: 
        currentIndex = names.index(lastNode)
    
    nextInput = input("Enter: ")
    
    if "<" in nextInput: #function to be able to backtrack, (need to fix, e.g. "jk<l" would cause error)
        if nextInput[1:] in nodes:
            lastNode = nextInput[1:] #takes input after the '<' as the node the user wants to backtrack to.
        else:
            print("Error - Node not already made. ") 
        #lastNode = names[currentIndex - len(nextInput)] (was initally used to back track a set number of steps rather than to a specific node.)
    elif nextInput == "exit": #function to complete node addition
        break
    
    else: #if input is not a special case, node addition can go ahead:

        if nextInput not in nodes:
            nodes[nextInput] = Node(nextInput)
            names.append(nextInput)

        if firstNode != True: #needed since first node cannot connect to nothing!
            nodes[nextInput].connector(lastNode)
            lastNode = nodes[nextInput].name()
        else: #hence if it is first node then it has no connections.
            firstNode = False
            lastNode = nextInput


#print(nodes) (prototyping feature)

#print(nodes['a'].connections)  (prototyping feature)

map1 = MindMap(nodes, names) #creates instance of a mind map.
map1.edges() #calls to create mindmap

graph.write_png("/tmp/test.png") #saves it in file (in /tmp/ for prototyping since saves in RAM)
