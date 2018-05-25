
#network - graph represented as dictionary {(u, v): value}
#startNmb - index of source
#verticesNmb - number of vertices
def modifyVertice(d, p, Q, v, u):
    if d[u] == -1: #equivalent of infinity
        d[u] = d[v] + 1
        p[u] = v
        Q.append(u)

def bfs(networkFlow, networkCapacity, p, startNmb):
    verticesNmb = len(networkCapacity)
    d = [-1] * verticesNmb
    p.extend([-1] * verticesNmb)

    Q = []
    Q.append(startNmb)

    while len(Q) != 0:
        v = Q.pop(0)
        for u in range(verticesNmb):#look for the v neighbour
            if networkFlow[v][u] != '*':#connection may exist
                remainingFlow = networkCapacity[v][u] - networkFlow[v][u]#cannot be equal 0
                if remainingFlow != 0:#cannot be 0?
                    modifyVertice(d, p, Q, v, u)
            elif networkFlow[u][v] != '*':#connection may exist in the opposite direction?(maybe after for loop??
                '''remainingFlow = networkCapacity[u][v] - networkFlow[u][v]
                if remainingFlow != 0:'''
                if networkFlow[u][v] != 0:
                    modifyVertice(d, p, Q, v, u)

            #check if connection exists
            if p[verticesNmb - 1] != -1:
                return True

    #connection with outpu doesnt exist
    return False

if __name__ == "__main__":
    bfs([], 0 , 5)