import sys
import math
import random

def INIT(G,s):
    d = [math.inf for i in range(len(G))]
    p = [None for i in range(len(G))]
    
    d[s] = 0
    return d, p
        
def RELAX(u, v, w, d, p):
    #print("d[{}]: {}, d[{}] {}, w {}".format(v,d[v],u ,d[u], w[u][v]))
    if d[v] > (d[u] + w[u][v]):
        
        d[v] = d[u] + w[u][v]
        p[v] = u
    
    return d, p

def Bellman_Ford(G, w, s):
    d, p = INIT(G, s)
    for i in range(len(G)-1):
        for u in range(len(G)):
            for v in range(len(G[0])):
                if G[u][v] != 0:
                    d, p = RELAX(u,v,w, d, p)
    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v] !=0:
                if d[v] > d[u] + w[u][v]:
                    print("F {}".format(d))
                    return ( False, d )
    return( True, d ,p)

if __name__ =='__main__':

    file = open(sys.argv[1], "r")

    #w sumie to MI
    data = [i.split() for i in file  if i != 'MI\n']
    #waga dl akażdego połączenia

    wagi = [random.randint(-5,10) for i in range(len(data))]
    #wagi = [5,8,4,-3,4,1,2]
    print(wagi)

    # w sumie to jest to lista sasiedztwa
    neigh = [[] for i in range(len(data[0]))]
    #print(neigh)
    for rec in data:
        z = rec.index('-1')
        do = rec.index('1')
        neigh[z].append(int(do))


    mas = [[ 0 for i in range(len(neigh))] for i in range(len(neigh))]
    #print("\n\n")
    #print(neigh)

    #print("\n\n")
    for u, g in enumerate(neigh):
        for v in g:
            mas[u][v] = wagi[v]
    
    """mas = [
        [0,4,5,8,0],
        [0,0,-3,0,0],
        [0,0,0,0,4],
        [0,0,0,0,2],
        [0,0,0,1,0]
        ]
    """
    for i in mas:
        print(i)
    print("\n\n")
    print(Bellman_Ford(mas, mas, 0)) 
