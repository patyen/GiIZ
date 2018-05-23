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


def ConvertToNeighbourMatrix(ls):
    matrix = [[0 for i in range(len(ls))] for j in range(len(ls))]

    for i in range(len(ls)):
        for j in range(len(ls[i])):
            matrix[i][ls[i][j]] = 1

    return matrix


def main():
    if len(sys.argv) < 2:
        print("prosze podac plik")
        sys.exit()

    fileName = sys.argv[1]
    ls = []
    ReadFile(ls, fileName)
    matrix = ConvertToNeighbourMatrix(ls)
    
    
    d = 0.15
    # ammount of vertices
    n = len(matrix)
    # ammount of iterations
    iters = 10**6
    

    # set degree of each vertex
    degree = [len(ls[i]) for i in range(len(ls))]    
    # set vector p0
    p = [[1/n for _ in range(n)]]
    # set stochastic matrix
    P = [[(1 - d)*matrix[i][j]/degree[i] + d/n for j in range(len(matrix[i]))] for i in range(len(matrix))]
 
    for t in range(1, iters):
        # vectors are in rows of p matrix
        p.append([])    
        # calculate p[t] vector            
        for j in range(n):
            # multiply p[t-1] * P matrix
            tmp = 0
            for h in range(n):
                tmp += p[t-1][h] * P[h][j]
            p[t].append(tmp)
    
    result = []
    for i in range(n):
        val = 0
        # calculate avarage value
        for j in range(len(p)):
            val += p[j][i]
        result.append(val/iters)

    print(result)




    
if __name__ == "__main__":
    main()