import sys
import distance_matrix as dm
import set3task2dijkstra as dij



def ReadFile(array, fileName):
    with open(fileName, 'r') as f:
        if f.readline().rstrip() != 'MS':
            print("prosze podac macierz sasiedztwa")
        for i in f:
            el = list(map(int, i.rstrip().split()))
            if len(el) > 1:
                array.append(el)


def GraphCenter(dist_matrix):

    if len(dist_matrix) == 0:
        print("pusta macierz odleglosci")
        return None

    vertex_index = 0
    min_dist = sum(dist_matrix[0])

    for i in range(1, len(dist_matrix)):
        if sum(dist_matrix[i]) < min_dist:
            min_dist = sum(dist_matrix[i])
            vertex_index = i
    
    print("Centrum Grafu - wierzcholek: {}, suma odleglosci: {}".format(vertex_index, min_dist))


def GraphMinimax(dist_matrix):
    if len(dist_matrix) == 0:
        print("pusta macierz odleglosci")
        return None

    
    vertex_index = 0
    max_dist = 10000000
    
    for i in range(len(dist_matrix)):
        if max_dist > max(dist_matrix[i]):
            vertex_index = i
            max_dist = max(dist_matrix[i])



    print("Minimax - wierzcholek: {}, najmniejsza maksymalna odleglosc: {}".format(vertex_index, max_dist))

def main():
    if len(sys.argv) < 2:
        print("prosze podac plik")
        sys.exit()
    
    fileName = sys.argv[1]
    matrix = []
    ReadFile(matrix, fileName)
    output = dm.DistanceMatrix(matrix)

    GraphCenter(output)
    GraphMinimax(output)





if __name__ == "__main__":
    main()