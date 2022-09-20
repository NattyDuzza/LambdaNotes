import pydot as pd
import os

graph = pd.Dot(graph_type="graph", rankdir="UD")

adj = []

for i in range(0, 10):

    # startingNode = int(input()) # Need to put it into hashing algorithm / list so as to be able to search for starting node efficiently
    done = False

    previousNode = i - 1
    name = input("Enter: ")


    for x in range(0, len(adj)):
        if name in adj[x]:
            print('double')
            adj[x].append(previousNode)
            done = True
            
    if done != True:        
        adj.append([name, previousNode])
    
print(adj)


for y in range(0, len(adj)):
    for x in range(1, len(adj[y])):
        if adj[y][x] != -1:
            edge = pd.Edge(adj[y][0], adj[(adj[y][x])][0])
            print(adj[y][0], adj[(adj[y][x])][0])
            graph.add_edge(edge)

graph.write_png("/tmp/test.png")

