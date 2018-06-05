import sys
import random

def ReadFile(array, fileName):
    with open(fileName, 'r') as f:
        if f.readline().rstrip() != 'MS':
            print("prosze podac macierz sasiedztwa")
            sys.exit()
        for i in f:
            el = list(map(int, i.rstrip().split()))
            if len(el) > 1:
                array.append(el)


def ShortestPath(matrix, n, max_it):
    for i in range(n):
        T = 0.001 * i**2
        for it in range(max_it -1, -1, -1):
            pass


def RandomCycle(matrix, start, successors):
    n = len(matrix)
    elements = [i for i in range(n)]
    index = start
    new_index = start
    length = 0
    elements.pop(index)
    print(elements)
    for i in range(n - 1):
        r = random.randrange(len(elements))
        new_index = elements[r]
        elements.pop(r)
        successors[index] = new_index
        length += matrix[index][new_index]
        index = new_index
    successors[index] = start
    length += matrix[index][start]
    print(length)    



def main():
    if len(sys.argv) < 2:
        print("prosze podac plik")
        sys.exit()
    
    fileName = sys.argv[1]
    matrix = []
    ReadFile(matrix, fileName)

    n = len(matrix)
    # for i in range(n):
    #     print(matrix[i])
    successors = [0 for _ in range(n)]

    RandomCycle(matrix, 0, successors)
    # ShortestPath(matrix, 10, 10)

    print(successors)


if __name__ == "__main__":
    main()