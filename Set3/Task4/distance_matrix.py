import sys
import set3task2dijkstra as dij

def ReadFile(array, fileName):
    with open(fileName, 'r') as f:
        if f.readline().rstrip() != 'MS':
            print("prosze podac macierz sasiedztwa")
        for i in f:
            el = list(map(int, i.rstrip().split()))
            if len(el) > 1:
                array.append(el)

def DistanceMatrix(matrix):
    output = []
    for i in range(len(matrix)):
        output.append(dij.dijkstra(matrix, i))
    return output

def main():

    if len(sys.argv) < 2:
        print("prosze podac plik")
        sys.exit()
    
    fileName = sys.argv[1]
    matrix = []
    ReadFile(matrix, fileName)

    output = DistanceMatrix(matrix)
        
    for i in output:
        print(i)

if __name__ == "__main__":
    #main()
    pass