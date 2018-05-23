import sys
import random

#N - number of layers(1...N) - except input and output
#layer 0 - input
#layer N+1 - output

#add an option to connect within one layer!!!

def printOutput(matrix):
    for row in matrix:
        for number in row:
            print(str(number), end=" ")
        print("")

def generateFlow(matrix):
    matrixSize = len(matrix)
    for row in range(matrixSize):
        for column in range(matrixSize):
            if matrix[row][column] == 1:
                matrix[row][column] = random.randrange(1, 11)

def connectionExist(matrix, fromVertice, destinationVertice):
    if matrix[fromVertice][destinationVertice] != 0:
        return True
    else:
        return False

def createListOfLayerVertices(currentLayer, layers):
    minIndex = sum(layers[:currentLayer])
    return list(range(minIndex, minIndex + layers[currentLayer]))

def createConnection(matrix, fromLayer, destinationLayer, layers):
    if destinationLayer == 0:#cannot create connection with the source
        return False


    fromVertices = createListOfLayerVertices(fromLayer, layers)
    destinationVertices = createListOfLayerVertices(destinationLayer, layers)

    randomFrom = random.choice(fromVertices)
    randomDestination = random.choice(destinationVertices)

    if not connectionExist(matrix, randomFrom, randomDestination):
        matrix[randomFrom][randomDestination] = 1
        return True
    else:
        return False

def createLayersConnections(matrixNetwork, fromVertices, destinationVertices):
    #first empty fromVertices(make all possible connections from)
    fromVerticesCopy = fromVertices[:]
    destinationVerticesCopy = destinationVertices[:]

    destinationEmptyFlag = False

    #iterate backwards so you won't get out of index
    for index in range(len(fromVertices) - 1, -1, -1):
        if destinationVertices:
            currentVerticeFrom = fromVertices.pop(index)#removes from list

            destinationIndex = destinationVertices.pop()#removes last item from list
            matrixNetwork[currentVerticeFrom][destinationIndex] = 1
        else:#destinationVertices is empty
            destinationEmptyFlag = True
            break


    #there are still some items in fromVertices but none in the destinationVertices
    offset = 0
    if destinationEmptyFlag:
        for index in range(len(fromVertices) - 1, -1, -1):
            currentVerticeFrom = fromVertices.pop(index)  # removes from list

            destinationIndex = destinationVerticesCopy[offset]
            offset += 1
            offset %= len(destinationVerticesCopy)
            matrixNetwork[currentVerticeFrom][destinationIndex] = 1
    else: #there is no more items in fromVertices but still are in the destinationVertices
        for index in range(len(destinationVertices) - 1, -1, -1):
                currentVerticeFrom = fromVerticesCopy[offset]
                destinationIndex = destinationVertices.pop(index)
                offset += 1
                offset %= len(fromVerticesCopy)
                matrixNetwork[currentVerticeFrom][destinationIndex] = 1


#row in the matrix indicates the beginning of connection and the column destination
def generateMatrixNetwork(layers, N):
    matrixNetwork = []
    #now we know how many vertices matrix contains (layers)
    verticesCount = 0

    for layer in layers:
        verticesCount += layer

    #create the empty matrixNetwork
    for vertice in range(verticesCount):
        matrixNetwork.append([0] * verticesCount)

    #generate connection to ensure that there's no isolated node and input is connected with output
    #lowest index from i layer
    lowestVerticeIndex = 0
    #i - current layer number
    for i in range(N + 1):
        #indexes from layer i that need connection
        fromVertices = list(range(lowestVerticeIndex, lowestVerticeIndex + layers[i]))
        #indexes from layer i+1 that need connection
        destinationVertices = list(range(lowestVerticeIndex + layers[i], lowestVerticeIndex + layers[i] + layers[i + 1]))
        createLayersConnections(matrixNetwork, fromVertices, destinationVertices)
        lowestVerticeIndex += layers[i]


    #adding random connections
    direction = ['r', 'l']
    randomCount = 2 * N

    while randomCount > 0:
        randomLayer = random.randrange(1, N + 1)
        randomDirection = random.choice(direction)

        if randomDirection == 'r':
            destinationLayer = randomLayer + 1
        elif randomDirection == 'l':
            destinationLayer = randomLayer - 1

        if createConnection(matrixNetwork, randomLayer, destinationLayer, layers):
            randomCount -= 1# reduce random vertices to add

    generateFlow(matrixNetwork)
    return matrixNetwork

def generateLayers(N):
    #1 is for input
    layers = [1]
    for layer in range(N):
        verticesInLayer = random.randrange(2, N + 1)
        layers.append(verticesInLayer)

    #for output
    layers.append(1)

    return layers

def generateNetwork(N):
    if N < 2:
        print("Too little layers provided")

    #generate each layer - number of vertices in them
    layers = generateLayers(N)

    #generate the matrix presenting this network
    matrixNetwork = generateMatrixNetwork(layers, N)
    print("layers")
    print(layers)
    print("matrix network")
    print(matrixNetwork)

    print("Output")
    printOutput(matrixNetwork)

if __name__ == "__main__":
    generateNetwork(int(sys.argv[1]))