import random
import sys


def ReadFile(ls, fileName):
    with open(fileName) as f:
        line = (str(f.readline()).rstrip())
        if line != "LS":
            print("Podaj liste sasiedztwa")
            sys.exit()
        for line in f:
            ls.append(line.rstrip().split(' '))

    for i in range(len(ls)):
        if len(ls[i]) > 0 and ls[i][0] != '':
            ls[i] = list(map(int, ls[i]))
        else:
            ls[i].remove('')




def main():
    if len(sys.argv) < 2:
        print("prosze podac plik")
        sys.exit()

    fileName = sys.argv[1]
    ls = []
    ReadFile(ls, fileName)

    # ammount of iterations
    n = 10**6
    # probability of teleportation
    d = 0.15
    # index of current vertex - starting with vertex of index 0
    index = 0
    # initialize result
    visited = [0 for i in range(len(ls))]

    for i in range(n):
        # set next move - teleportation or go to one of neighbours of current vertex
        nextMove = random.uniform(0,1)
        # notice the visitation of the index
        visited[index] += 1
        # go to a neighbour
        if nextMove > d and len(ls[index]) > 0:
            index = random.choice(ls[index])
        # teleport
        else:
            index = random.choice(range(len(ls)))         




    for i in range(len(visited)):
        visited[i] = visited[i] / n
    print(visited)





if __name__ == "__main__":
    main()