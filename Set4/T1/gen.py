import sys
import random

n = int(sys.argv[1])
p = float(sys.argv[2])
input_good = True

if n < 2 or p > 1 or p < 0:
    input_good = False

if not input_good:
    print("bad input")
else:
    verts = [i for i in range(n)]
    connections = []
    no_connections = True
    for v1 in verts:
        for v2 in verts:
            if v1 != v2:
                r = random.random()
                if r <= p:
                    connections.append([v1,v2])
    if len(connections) != 0:
        no_connections = False
    
    if no_connections:
        pass
    else:
        print(connections)
        file = open("graph_out.txt", "w")
        for con in connections:
            row = ['0' for i in range(n)]
            row[con[0]] = -1
            row[con[1]] = 1
            for c in row:
                file.write("{} ".format(c))
            file.write("\n")
