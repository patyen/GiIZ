import random
from Task1 import check_graphical_sequence


def randomSequence(vertices):
    # sum of degrees for each vertice must be even
    # vertice debree < number of vertices
    # for euler graph each vertice degree must be even
    #vertices must be at least 2! - i think
    sequence = []

    for verticeNmb in range(vertices):
        generatedDegree = random.randint(2, vertices - 1)
        if generatedDegree % 2 == 1:
            sequence.append(generatedDegree - 1)
        else:
            sequence.append(generatedDegree)

    return sequence


#it assumes that this is graphical sequence and creates an adjacency matrix
def createAdjacencyMatrix(sequence):
    sequence = sorted(sequence, reverse=True)
    vertices = len(sequence)

    #print(sequence)

    sequenceNodes = [[nodeNmb, degree] for nodeNmb, degree in enumerate(sequence)]
    #[[node1,connections1],...,[noden,connectionsn]]
    #print(sequenceNodes)

    adjacencyMatrix = []

    #first generate an empty matrix
    for i in range(vertices):
        adjacencyMatrix.append([0] * vertices)


    #while there are still some connections possible (it's sorted so we can take first element)
    while sequenceNodes[0][1] > 0:
        connectionNumber = sequenceNodes[0][1]
        sequenceNodes[0][1] = 0#zero current node connection
        neighbourOffset = 1
        while connectionNumber > 0:
            if sequenceNodes[neighbourOffset][1] > 0:
                currentNode = sequenceNodes[0][0]#number of current node
                currentNeighbour = sequenceNodes[neighbourOffset][0]#number of node with which we currently create a connection
                adjacencyMatrix[currentNode][currentNeighbour] = 1
                adjacencyMatrix[currentNeighbour][currentNode] = 1
                sequenceNodes[neighbourOffset][1] -= 1
                connectionNumber -= 1

            neighbourOffset += 1

        sequenceNodes = sorted(sequenceNodes, key=lambda l: l[1], reverse=True)

    return adjacencyMatrix


def componentsR(nr, node, graph, comp):
    for nodeNeighbour in graph[node - 1]:
        if comp[nodeNeighbour] == -1:
            comp[nodeNeighbour] = nr
            componentsR(nr, nodeNeighbour, graph, comp)


#it's Components algorithm
def checkBridge(graph):
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

    if(nr == 1):
        return False #there's no bridge
    else:
        return True


#https://stackoverflow.com/questions/1593564/python-how-to-check-if-a-nested-list-is-essentially-empty
def isListEmpty(inList):
    if isinstance(inList, list): # Is a list
        return all( map(isListEmpty, inList) )
    return False # Not a list

#it checks if it's bridge if it is then it's looking for other option which is not a bridge(but still
#holds bridge possibility
def findEuler(graph, tour):
    currentNode = 1

    while not isListEmpty(graph): #while list is not empty
        if(len(graph[currentNode - 1]) == 0):#if current node has no neighbours anymore
            return False

        bridgeFlag = False
        #it iterates through  neighbours of current node
        for neighbour in graph[currentNode - 1]:
            #print(graph)
            graph[currentNode - 1].remove(neighbour)
            graph[neighbour - 1].remove(currentNode)# remove current node from the neighbour

            if checkBridge(graph):  # looks for node that won't create a bridge
                #it restores the previous state
                graph[currentNode - 1].insert(0, neighbour)
                graph[neighbour - 1].insert(0, currentNode)

                newNodeRemember = neighbour
                bridgeFlag = True
            else:
                bridgeFlag = False
                break

        #we leave the current node so add it to path
        tour.insert(0, currentNode)

        #if we are crossing the bridge
        if bridgeFlag:
            graph[currentNode - 1].remove(newNodeRemember)
            graph[neighbour - 1].remove(currentNode)
            currentNode = newNodeRemember

        currentNode = neighbour

    tour.insert(0, currentNode) #add last node
    return True


if __name__ == "__main__":
    # default number of vertices in the graph
    vertices = 7

    sequence = []
    while True:
        sequence = randomSequence(vertices)
        if check_graphical_sequence.calculateSequence(sequence):
            break

    print("Wygenerowana sekwencja")
    print(sequence)
    adjacencyMatrix = createAdjacencyMatrix(sequence)
    print("W formie macierzy sąsiedztwa")
    print(adjacencyMatrix)

    #print(createAdjacencyMatrix([4, 4, 2, 4, 4, 4, 6]))
    #adjacencyMatrix = createAdjacencyMatrix([4, 4, 2, 4, 4, 4, 6])

    #print(createAdjacencyMatrix([4, 2, 2, 2, 4, 6, 2]))
    #adjacencyMatrix = createAdjacencyMatrix([4, 2, 2, 2, 4, 6, 2])

    #neighbourList conversion
    neighbourList= [ [ vertex + 1 for vertex in range(len(row)) if row[vertex] ]for row in adjacencyMatrix]

    tour = []
    print(findEuler(neighbourList, tour))
    print(tour)