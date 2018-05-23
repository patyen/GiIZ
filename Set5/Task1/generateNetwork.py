import sys
import random

#N - number of layers(1...N) - except input and output
#layer 0 - input
#layer N+1 - output

def printOutput(matrix):
    for row in matrix:
        for number in row:
            print(str(number), end=" ")
        print("")


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

    print(fromVertices)
    print(destinationVertices)

    #there are still some items in fromVertices but none in the destinationVertices
    # should it check if connection already exists? (is it possible?)
    # maybe i've messed up with flags?
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

    #lowest index from i layer
    lowestVerticeIndex = 0

    #i - current layer number
    for i in range(N + 1):
        #indexes from layer i that need connection
        fromVertices = list(range(lowestVerticeIndex, lowestVerticeIndex + layers[i]))
        #indexes from layer i+1 that need connection
        destinationVertices = list(range(lowestVerticeIndex + layers[i], lowestVerticeIndex + layers[i] + layers[i + 1]))
        print("iteration" + str(i))
        print("from vertices")
        print(fromVertices)
        print("destination vertices")
        print(destinationVertices)
        createLayersConnections(matrixNetwork, fromVertices, destinationVertices)
        lowestVerticeIndex += layers[i]

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