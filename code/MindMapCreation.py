import pydot as pd #imports package needed for mindmap output


#Class Node is the class that will be a blueprint for every 'node' of data on the mind map. 
class Node: 
    def __init__(self, name):
        self._name = name 
        self.connections = [] #this is where the connected nodes to each instance will be stored.

    def name(self): #makes it easier to access the name of each object.
        return self._name 

    def connector(self, previousNode): 
        self.connections.append(previousNode) #adds the previous node (hence the node the instance which is using this function was connected onto) to the connections list
       

#Class MindMap is a class that will handle the initialisation of a new mindmap and contructs it once all the nodes have been added. Not much use for now since we are only creating one mindmap but will be helpful when we move to full development.
class MindMap:
    def __init__(self, nodes, names, graph):
        self._nodes = nodes
        self._names = names
        self._graph = graph

    def edges(self):
        for i in range(0, len(self._names)): #iterates through the length of the list of node names (not happy with doing it this way)
            parent = self._nodes[self._names[i]].name() #sets the parent of the connection to the node with the name at the index i. Hence all nodes will be iterated over in this way.
            for j in range(0, len(self._nodes[self._names[i]].connections)): #iterates over the list of connections to the parent node
                edge = pd.Edge(parent, self._nodes[self._names[i]].connections[j]) #creates edge between parent and current node (at index j in the nodes connection list)
                self._graph.add_edge(edge) #adds edge to graph
        return self._graph
    
class Maker:
    def __init__(self):
        self.graph = pd.Dot(graph_type="graph", rankdir="UD")
        self.nodes = {}
        self.names = []
        self.count = 0
        self.lastNode = 0
        self.firstNode = True
        self.errorChecker = False

    def input(self, backtrack, instance):
    
        if self.lastNode != 0: 
            currentIndex = self.names.index(self.lastNode)
        
        nextInput = instance.nodeName.get()
        
        if backtrack == True: #function to be able to backtrack, (need to fix, e.g. "jk<l" would cause error)
            if nextInput in self.nodes:
                self.lastNode = nextInput #takes input after the '<' as the node the user wants to backtrack to.
                if self.errorChecker == True:
                    instance.errorLabel.config(text="")
            else:
                instance.errorLabel.config(text="Node not already in Mind Map") 
                self.errorChecker = True
        
        else: #if input is not a special case, node addition can go ahead:
            if self.errorChecker == True:
                    instance.errorLabel.config(text="")

            if nextInput not in self.nodes:
                self.nodes[nextInput] = Node(nextInput)
                self.names.append(nextInput)

            if self.firstNode != True: #needed since first node cannot connect to nothing!
                self.nodes[nextInput].connector(self.lastNode)
                self.lastNode = self.nodes[nextInput].name()
            else: #hence if it is first node then it has no connections.
                self.firstNode = False
                self.lastNode = nextInput

    def create(self):
        self.map = MindMap(self.nodes, self.names, self.graph)
        self.graph = self.map.edges()

    def output(self):
        self.graph.write_png("/tmp/test.png")





