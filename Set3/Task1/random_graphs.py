from sys import argv
from sys import exit
from random import randint, uniform, choice

from Matrix_Conversion import Matrix

#niech oblicza wagi na koncu

def createWeighted(weighted):
    matrixLength = len(weighted)

    for i in range(matrixLength):
        for j in range(matrixLength):
            if(weighted[i][j] == 1):
                randomNumber = randint(1, 10)
                weighted[i][j] = randomNumber
                weighted[j][i] = randomNumber

#trzeba pozbyć się izolowanych punktów
def swapVertices(data):
    #print("INPUT")
   # print (data)

    flag = 1
    data_size = len(data)

    #print("DATA SIZE")
    #print(data_size)

    if data_size > 2:
        while flag:
            #print("flag number of data", len(data))
            first_index = choice(range(len(data)))
            second_index = choice(range(len(data)))
            #select different ledge
            while first_index == second_index:
                #print("infinity")
                #print("lengthof data", len(data))
                second_index = choice(range(len(data)))


            tmp1 = data[first_index]
            tmp2 = data[second_index]

            #print(tmp1)

            back1 = tmp1[:]
            back2 = tmp2[:]

            #to prevent trouble with removed indexes
            if (first_index < second_index):
                data.pop(second_index)
                data.pop(first_index)
            else:
                data.pop(first_index)
                data.pop(second_index)

            zipped = zip(tmp1, tmp2)
            flag = 0

            #connection with this same vertice
            if (1, 1) in zipped:
                flag = 1
                data.append(back1)
                data.append(back2)
                continue # my change

            n_index_one = tmp1.index(1)
            n_index_two = tmp2.index(1)

            #swap vertices
            tmp1[n_index_one] = 0
            tmp2[n_index_two] = 0

            tmp1[n_index_two] = 1
            tmp2[n_index_one] = 1

            #print("loop")

            #if this connection already exists
            if tmp1 in data or tmp2 in data:
                flag = 1
                data.append(back1)
                data.append(back2)
            else: #this connection is unique
                data.append(tmp1)
                data.append(tmp2)

#input - neighbour list
def isolatedIndex(graph):
    #print("ISOLATED")
    for vertice in range(len(graph)):
        if len(graph[vertice]) == 0:
            return vertice
    return -1

#nie musi sprawdzać czy łączony izolowany
#excepcts neighbour list
def connectIsolated(graph, indexOfIsolated):
    verticeToReplaceIndex = choice(range(len(graph)))

    while verticeToReplaceIndex == indexOfIsolated:
        verticeToReplaceIndex = choice(range(len(graph)))

    #point is isolated or will be isolated after replace
    if len(graph[verticeToReplaceIndex]) <= 1:
        return graph

    #print(graph[verticeToReplaceIndex])
    #connect with selected vertice
    graph[indexOfIsolated].append(verticeToReplaceIndex + 1)
    graph[verticeToReplaceIndex].append(indexOfIsolated + 1)

    #print(graph[verticeToReplaceIndex])

    #remove first found vertice
    returnedIndex = graph[verticeToReplaceIndex].pop(0) - 1 #to get number of index it need to substract 1

    #print(returnedIndex, indexOfIsolated, verticeToReplaceIndex, graph[returnedIndex],
    #      graph[indexOfIsolated], graph[verticeToReplaceIndex])
    graph[returnedIndex].remove(verticeToReplaceIndex + 1 )

    #print(graph)
    #print("END of isolated")

    return graph
'''
    #choose which vertex to modify
    ledgeToReplaceIndex = choice(range(len(graph)))

    while ledgeToReplaceIndex == indexOfIsolated:
        ledgeToReplaceIndex = choice(range(len(graph)))

    ledgeToReplace = graph[ledgeToReplaceIndex]

    print("ledge to replace")
    print(ledgeToReplace)

    #it's also isolated
    if 1 not in ledgeToReplace:
        return

    indexOfVertice = ledgeToReplace.index(1)
    ledgeToReplace[indexOfVertice] = 0

    #end of isolation
    ledgeToReplace[indexOfIsolated] = 1
'''

# create a file
def CreateFile(vertices, length):
    file = open("graph.out", "w")

    
    #file.write("{}\n".format("MS"))

    for i in range(length):
        for j in range(length):
            file.write("{} ".format(vertices[i][j], " "))
        file.write("{}".format('\n'))

    file.close()

def componentsR(nr, node, graph, comp):
    for nodeNeighbour in graph[node - 1]:
        if comp[nodeNeighbour] == -1:
            comp[nodeNeighbour] = nr
            componentsR(nr, nodeNeighbour, graph, comp)

#it's Components algorithm
def components(graph):
    nr = 0
    #create a dictionary which hold number of node and part of graph to which it belongs
    comp = {}
    for node in range(1, len(graph) + 1):
        comp[node] = -1

    for node in range(1, len(graph) + 1):
        if comp[node] == -1:
            nr += 1
            comp[node] = nr
            componentsR(nr, node, graph, comp)

    return nr

def createRandom(vertexCount):
    vertices = [[0 for i in range(vertexCount)] for j in range(vertexCount)]

    # generate graph with given number of ledges
    if argv[1] == 'l':
        ledgeCount = int(argv[2])

        # check if it's possible to create that graph with given parameters
        if vertexCount * (vertexCount - 1) / 2 <= ledgeCount:
            print("Za duzy stosunek wierzcholkow do krawedzi")
            exit()

        if ledgeCount < vertexCount - 1:
            print("Za mala liczba krawedzi")
            exit()

        n = 0
        while n < ledgeCount:

            # get random numbers in range of number of vertices
            x = randint(0, vertexCount - 1)
            y = randint(0, vertexCount - 1)

            # check if already not connected and if it's not a diagonal
            if vertices[y][x] == 0 and x != y:
                #verticeWeight = randint(1, 10)
                vertices[y][x] = 1
                vertices[x][y] = 1
                n += 1
    elif argv[1] == 'p':
        probability = float(argv[2])

        countConnection = 0

        for i in range(vertexCount):
            # start with i + 1 because the rest is already set
            for j in range(i + 1, vertexCount):
                x = uniform(0.0, 1.0)
                if x < probability:
                    #verticeWeight = randint(1, 10)
                    vertices[j][i] = 1
                    vertices[i][j] = 1
                    countConnection += 1
        #too little ledges
        if countConnection < vertexCount - 1:
            print("Wygenerowano graf ze zbyt mala liczba krawedzi, aby mozliwe bylo wygereowanie"
                  "grafu spojnego")
            exit()
    else:
        print("Prosze podac: l lub p, liczbe krawedzi lub prawdopodobienstwo oraz liczbe wierzcholkow")
        exit()

    return vertices

def connectiveGraph():
    # check if valid arguments
    if len(argv) != 4:
        print("Prosze podac: l lub p, liczbe krawedzi lub prawdopodobienstwo oraz liczbe wierzcholkow HE")
        exit()

    # number of vertices
    vertexCount = int(argv[3])
    iterations = 0

    vertices = createRandom(vertexCount)
    #at beginning as adjacement matrix
    graph = Matrix(vertices, "MS")
    #to check components neighbour list is needed
    graph.convert_matrix("LS")

    print("VERTICES")
    print(vertices)
    print("NEIGHBOUR")
    print(graph._content)
    print("SKLADOWE")
    print(components(graph._content))




    while components(graph._content) != 1:
        #print("iteration number")
        #print(iterations)

        if iterations >= 1000:
            print("Nie udalo sie utworzyc grafu spojnego o zadanych parametrach")
            print(components(graph._content))
            graph.convert_matrix("LS")
            graph.print_matrix()
            exit()

        while True:
            isolated = isolatedIndex(graph._content)
            if isolated == -1:
                break
            connectIsolated(graph._content, isolated)
            #graph.print_matrix()
            #print(connectIsolated(graph._content, isolated))
            #graph.print_matrix()
            #print("there is an isolated point")
            #print(isolated)

        #swap uses incidention
        #print("matrix conversion line 190")
        graph.convert_matrix("MI")
        #print("before swapping")
        #print(graph._content)
        swapVertices(graph._content)
        #print("end of swap")
        #and then again to neighbour list to check components
        graph.convert_matrix("LS")
        #print(graph._content)
        iterations += 1

    graph.convert_matrix("MS")

    weighted = graph._content[:]

    createWeighted(weighted)

    graph.convert_matrix("MI")
    #output matrix.out
    graph.write_matrix_to_file()




    CreateFile(weighted, vertexCount)


if __name__ == "__main__":
    connectiveGraph()