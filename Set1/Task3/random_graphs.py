from sys import argv
from sys import exit
from random import randint
from random import uniform


# create a file
def CreateFile(vertices, length):
    file = open("graph.out", "w")
    
    file.write("{}\n".format("MS"))

    for i in range(length):
        for j in range(length):
            file.write("{} ".format(vertices[i][j], ' '))
        file.write("{}".format('\n'))



    file.close()




# check if valid arguments
if len(argv) != 4:
    print("Prosze podac: l lub p, liczbe krawedzi lub prawdopodobienstwo oraz liczbe wierzcholkow HE")
    exit()

# number of vertices
vertexCount = int(argv[3])
vertices = [[0 for i in range(vertexCount)] for j in range(vertexCount)]


# generate graph with given number of ledges
if argv[1] == 'l':
    ledgeCount = int(argv[2])

    # check if it's possible to create that graph with given parameters
    if vertexCount * (vertexCount - 1) / 2 <= ledgeCount:
        print("Za duzy stosunek wierzcholkow do krawedzi")
        exit()
    


    n = 0
    while n < ledgeCount:
        
        # get random numbers in range of number of vertices
        x = randint(0, vertexCount - 1)
        y = randint(0, vertexCount - 1)

        # check if already not connected and if it's not a diagonal
        if vertices[y][x] == 0 and x != y:
            vertices[y][x] = 1
            vertices[x][y] = 1            
            n += 1

    
    CreateFile(vertices, vertexCount)
    
            
elif argv[1] == 'p':
    probability = float(argv[2])
    
    
    for i in range(vertexCount):
        # start with i + 1 because the rest is already set
        for j in range(i + 1, vertexCount):
            x = uniform(0.0, 1.0)
            if x < probability:
                vertices[j][i] = 1
                vertices[i][j] = 1
    

    CreateFile(vertices, vertexCount)
else:
    print("Prosze podac: l lub p, liczbe krawedzi lub prawdopodobienstwo oraz liczbe wierzcholkow")    
    exit()
