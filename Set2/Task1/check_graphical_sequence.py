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

def calculateSequence(sequence):

    #usuwać zera
    #sortować
    #brać pierwszy element
    #jeżeli lista zostanie pusta(same zera) to true
    #jeżeli zostanie jeden niezerowy element to nie jest ciągiem graficznym
    #jeżeli wyjdzie poza zakres listy przy odejmowaniu, np ciąg 4 3 to też fałsz

    while(len(sequence)>1):
        sequence = sorted(sequence, reverse=True)

        print("Poczatek petli")

        print(sequence)

        while 0 in sequence:#usuń zera z listy
            sequence.remove(0)

        print(sequence)

        if (len(sequence) == 0):
            return True

        edge_nmb = sequence[0]
        sequence[0] = 0


        cur_vertex = 1
        while (edge_nmb > 0):
            if (cur_vertex >= len(sequence)):
                return False  # nie jest graficzny, wyszlo poza zakres//

            sequence[cur_vertex] -= 1
            cur_vertex += 1  # przejscie do kolejnego wierzcholka
            edge_nmb -= 1  # zmniejszona liczba polaczen


    return False


if __name__  == "__main__":
    sequence = [ int(x) for x in input().split()]

    print(sequence)

    if calculateSequence(sequence):
        print("Jest ciagiem graficznym")
        adjacencyMatrix = createAdjacencyMatrix(sequence)
        print(adjacencyMatrix)

        #creating incedency matrix
        tmp = []
        matrix_length = len(adjacencyMatrix)

        for col_nmb in range(matrix_length):
            for row_nmb in range(col_nmb, matrix_length):
                if (adjacencyMatrix[row_nmb][col_nmb]):  # jeżeli znaleziono krawędź
                    tmp.append([1 if (i == row_nmb or i == col_nmb) else 0 for i in range(matrix_length)])
        #write it to a file
        output = open("matrix.out", "w")

        print("MI", file = output)
        for vertex in range(len(tmp)):
            print(*tmp[vertex], file = output)

    else:
        print("Nie jest ciagiem graficznym")
