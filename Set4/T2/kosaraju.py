import sys

file = open(sys.argv[1], "r")


data = [i.split() for i in file  if i != 'MI\n']

# w sumie to jest to lista sasiedztwa
neigh = [[] for i in range(len(data[0]))]
#lista sasiedztwa tego grafu po transpozycji
neigh_T = [[] for i in range(len(data[0]))]
for rec in data:
    z = rec.index('-1')
    do = rec.index('1')
    neigh[z].append(int(do))

print(neigh)

for rec in data:
    do = rec.index('-1')
    z = rec.index('1')
    neigh_T[z].append(int(do))



def DFS_visit(v, G, d, f, t):
    
    t += 1
    d[v] = t
    for u in G[v]:
        if d[u] == -1:
            t = DFS_visit(u, G, d, f, t)
    t +=  1
    f[v] = t
    return t

def Components_R(nr,v, Gt,comp):
    for u in Gt[v]:
        if comp[u] == -1:
            comp[u] = nr
            Components_R(nr, u, Gt, comp)


def Kossaraju(G, Gt):
    d = [-1 for i in range(len(G))]
    f = [-1 for i in range(len(G))]
    t = 0

    for v in range(len(G)):
        if d[v] == -1:
             t = DFS_visit(v, G, d, f, t)
    
    print(d)
    #graf transponowany
    nr = 0
    comp = [-1 for i in range(len(Gt))]
    for dt in range(len(d)):
        v = d.index(max(d)) 
        d.pop(v)
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            Components_R(nr, v, Gt, comp)
    return comp

print("wsp składowe : {}".format(Kossaraju(neigh, neigh_T)))
