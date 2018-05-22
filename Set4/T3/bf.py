import sys
import math
import random

def INIT(G,s):
    d = [math.inf for i in range(len(neigh))]
    p = [None for i in range(len(neigh))]
    
    d[s] = 0
    return d, p
        
def RELAX(u, v, w, d, p):
    if d[v] > (d[u] + w[u][v]):
        d[v] = d[u] + w[u][v]
        p[v] = u
    return d, p

def Bellman_Ford(G, w, s):
    d, p = INIT(G, s)
    for i in range(len(neigh)-1):
        for u in range(len(mas)):
            for v in range(len(mas[0])):
                if mas[u][v] != 0:
                    RELAX(u,v,w, d, p)
    for u in range(len(mas)):
        for v in range(len(mas)):
            if mas[u][v] !=0:
                if d[v] > d[u] + w[u][v]:
                    print("F {}".format(d))
                    return ( False, d )
    return( True, d )

if __name__ =='__main__':

    file = open(sys.argv[1], "r")

    #w sumie to MI
    data = [i.split() for i in file  if i != 'MI\n']
    #waga dl akażdego połączenia

    wagi = [random.randint(-5,10) for i in range(len(data))]
    wagi = [11 for i in range(len(data))]
    #print(wagi)

    # w sumie to jest to lista sasiedztwa
    neigh = [[] for i in range(len(data[0]))]
    #print(neigh)
    for rec in data:
        z = rec.index('-1')
        do = rec.index('1')
        neigh[z].append(int(do))


    mas = [[ 0 for i in range(len(neigh))] for i in range(len(neigh))]
    #print(len(neigh))
    for u, g in enumerate(neigh):
        for v in g:
            mas[u][v] = wagi[u]

    print(Bellman_Ford(mas, mas, 0)) 
