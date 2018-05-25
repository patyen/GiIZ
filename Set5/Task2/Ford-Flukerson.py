import sys
import copy
import bfs

'''
#add existing connection to dict
def prepareEdgesCapacity(matrix):
    matrixLength = len(matrix)

    edgesCapacity = []

    for fromVert in range(matrixLength):
        for destVert in range(matrixLength):
            if(matrix[fromVert][destVert] != 0):
                edgesCapacity.append([(fromVert, destVert), matrix[fromVert][destVert]])

    return edgesCapacity
'''

#it sums whole capacity of the network and adds 1 to get something which can be treated as infinity in that case
def getInfinity(networkCapacity):
    result = 0
    for row in networkCapacity:
        result += sum(row)
    return result + 1

def getMinimumResidualCap(networkFlow, networkCapacity, p):
    verticesNmb = len(networkCapacity)
    currentVertice = verticesNmb - 1  # start from the output

    minResidualCapacity = getInfinity(networkCapacity)

    #as long as you won't find the source
    while currentVertice != 0:
        previousVertice = p[currentVertice]
        foundFlag = False

        #print("previous")
        #print(previousVertice)

        if networkFlow[currentVertice][previousVertice] != '*':  # connection exist from current to previous
            connectionCapacity = networkCapacity[currentVertice][previousVertice] - networkFlow[currentVertice][previousVertice]
            if connectionCapacity != 0: #there's still remaining flow, so connection is possible
                foundFlag = True

        if foundFlag == False: # connection exist from previous to current
            connectionCapacity = networkCapacity[previousVertice][currentVertice] - networkFlow[previousVertice][currentVertice]


        if connectionCapacity < minResidualCapacity:#if found the lowest capacity in the path
            minResidualCapacity = connectionCapacity

        #print(connectionCapacity)
        #print(foundFlag)

        currentVertice = previousVertice#move backwards

    return minResidualCapacity


def FordFulkerson(networkCapacity):
    verticesNmb = len(networkCapacity)
    networkFlow = [[ 0 if value else '*' for value in row] for row in networkCapacity ]

    print(networkCapacity)
    print(networkFlow)

    p = []

    while bfs.bfs(networkFlow, networkCapacity, p, 0):#line 3
        minResidualCapacity = getMinimumResidualCap(networkFlow, networkCapacity, p)#line 4
        currentVertice = verticesNmb - 1#start from the output

        print(p)
        print(minResidualCapacity)

        while currentVertice != 0: #line 5
            modified = False
            previousVertice = p[currentVertice]

            if networkFlow[previousVertice][currentVertice] != '*':  #if(u,v vertice exist)
                connectionCapacity = networkCapacity[previousVertice][currentVertice] - networkFlow[previousVertice][currentVertice]
                if connectionCapacity != 0:  # there's still remaining flow, so connection is possible
                    networkFlow[previousVertice][currentVertice] += minResidualCapacity
                else:#I am not quite sure
                    networkFlow[previousVertice][currentVertice] -= minResidualCapacity
                    #maybe here another -= minResidual?
                modified = True

            if modified == False: #connection doesnt exist or there's no reamining flow
                networkFlow[currentVertice][previousVertice] -= minResidualCapacity

            currentVertice = previousVertice

        for row in networkFlow:
            print(row)

            '''
            if networkFlow[currentVertice][previousVertice] != '*':  # connection exist from current to previous
                connectionCapacity = networkCapacity[currentVertice][previousVertice] - networkFlow[currentVertice][
                    previousVertice]
                if connectionCapacity != 0:  # there's still remaining flow, so connection is possible
                    networkFlow[currentVertice][previousVertice] -= minResidualCapacity #are index correct?
                    modified = True

            if modified == False:  # connection exist from previous to current
                connectionCapacity = networkCapacity[previousVertice][currentVertice] - networkFlow[previousVertice][
                    currentVertice]
                networkFlow[previousVertice][currentVertice] += minResidualCapacity
            '''


        p = [] #clear p for the bfs

    print("output")
    for row in networkFlow:
        print(row)

if __name__ == "__main__":
    matrix = []

    with open(sys.argv[1]) as file:
       for line in file:
           matrix.append([int(x) for x in line.split()])

    FordFulkerson(matrix)