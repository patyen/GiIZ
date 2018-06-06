import sys
import random
import math
import copy






def ReadFile(array, fileName):
    with open(fileName, 'r') as f:
        if f.readline().rstrip() != 'MS':
            print("prosze podac macierz sasiedztwa")
            sys.exit()
        for i in f:
            el = list(map(int, i.rstrip().split()))
            if len(el) > 1:
                array.append(el)




def RandomCycle(cycle, start, length):
    cycle.append(start)
    while len(cycle) != length:
        x = random.randint(0, length - 1)
        if x not in cycle:
            cycle.append(x)




def IsConsistent(cycle):
    visited = [0 for i in range(len(cycle))]
    for i in range(len(cycle)):
        visited[i] += 1
    if 0 not in visited:
        return True
    return False


def CalculateLength(matrix, cycle):
    length = 0
    for i in range(len(cycle) - 1):
        length += matrix[cycle[i]][cycle[i+1]]
    length += matrix[cycle[len(cycle) - 1]][cycle[0]]
    return length


def ShortestPath(matrix, cycle, n, max_it):
    l = len(matrix)
    cycle_len = CalculateLength(matrix, cycle)
    for i in range(n - 1, 0, -1):
        T = 0.001 * i*i
        for _ in range(0, max_it):
            temp_cycle = copy.deepcopy(cycle)
            while True:
                # ledges = []
                # for _ in range(4):
                    # ledges.append(random.randint(0, l-1))
                vertex1 = random.randint(0, l-1)
                vertex2 = vertex1 + 1                
                if vertex1 == l - 1:
                    vertex2 = 0
                    
                vertex3 = random.randint(0, l-1)
                vertex4 = vertex3 + 1
                if vertex3 == l - 1:
                    vertex4 = 0
                temp = temp_cycle[vertex2]
                temp_cycle[vertex2] = temp_cycle[vertex4]
                temp_cycle[vertex4] = temp
                
                
                if IsConsistent(temp_cycle):
                    break
            new_cycle_len = CalculateLength(matrix, temp_cycle)
            if new_cycle_len < cycle_len or random.uniform(0, 1) < math.exp(-(new_cycle_len - cycle_len) / T) :
                cycle = copy.deepcopy(temp_cycle)
                cycle_len = new_cycle_len
        # print(cycle)
    return cycle

            
    


def main():
    if len(sys.argv) < 2:
        print("prosze podac plik")
        sys.exit()
    
    fileName = sys.argv[1]
    matrix = []
    ReadFile(matrix, fileName)

    n = len(matrix)    

    cycle = []    
    RandomCycle(cycle, 0, n)

    newCycle = ShortestPath(matrix, cycle, 20, 20)

    print("Cykl wylosowany\n", cycle, "Dlugosc:", CalculateLength(matrix, cycle))
    print("Po uzyciu algorytmu\n", newCycle, "Dlugosc:", CalculateLength(matrix, newCycle))
    # print(cycle)
    
    # print(CalculateLength(matrix, cycle))
    # print(IsConsistent(cycle))


if __name__ == "__main__":
    main()