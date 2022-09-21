import pydot as pd
import os

graph = pd.Dot(graph_type="graph", rankdir="UD")

adj = []



    # startingNode = int(input()) # Need to put it into hashing algorithm / list so as to be able to search for starting node efficiently
done = False

k = 0

while k < 11 or len(adj) == 0:
    name = input("Enter: ")
    previousNode = k - 1

    done = False

    for i in range(0, len(adj)):

        if name in adj[i]:
            print('double')
            adj[i].append(previousNode)
            k = i

        

            done = True
            
    if done != True:        
        adj.append([name, previousNode])
 
    k += 1
print(adj)


for y in range(0, len(adj)):
    for x in range(1, len(adj[y])):
        if adj[y][x] != -1:
            edge = pd.Edge(adj[y][0], adj[(adj[y][x])][0])
            print(adj[y][0], adj[(adj[y][x])][0])
            graph.add_edge(edge)

graph.write_png("/tmp/test.png")

