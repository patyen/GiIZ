import sys

def ReadFile(array, fileName):
    with open(fileName, 'r') as f:
        if f.readline().rstrip() != 'MS':
            print("prosze podac macierz sasiedztwa")
        for i in f:
            el = list(map(int, i.rstrip().split()))
            if len(el) > 1:
                array.append(el)


def Prim(matrix, vertex_to_start):
    heap_map = [100000 for i in range(len(matrix))]
    heap_map[vertex_to_start] = 0

    length = len(matrix)

    # tablica poprzednikow
    p = [0 for i in range(len(matrix))]

    # tablica gotowych wierzcholkow
    ready_vertices = []

    # obecny index na ktorym wykonywane sa operacje
    index = vertex_to_start

    while len(ready_vertices) != length:
        for i in range(len(matrix[index])):
            # sprawdzam czy wierzcholek juz nie jest gotowy i
            # czy jest polaczenie miedzy wierzcholkami
            if i not in ready_vertices and matrix[index][i] != 0:
                # jezeli nowe polaczenie miedzy danym wierzcholkiem i
                # jakas krawedzia lepsze(krotsze) to zamieniam poprzednika
                if matrix[index][i] < heap_map[i]:
                    heap_map[i] = matrix[index][i]
                    p[i] = index
        # dodaje wierzcholek do gotowych
        ready_vertices.append(index)
        # sztucznie usuwam z heap_map
        heap_map[index] = 100000
        # wybieram nowy indeks - minimalny
        index = heap_map.index(min(heap_map))

    # wierzcholek poczatkowy
    p[vertex_to_start] = 'x'    

    print(p)




def main():
    if len(sys.argv) < 2:
        print("prosze podac plik")
        sys.exit()
    
    fileName = sys.argv[1]
    matrix = []
    
    ReadFile(matrix, fileName)

    #print(matrix[1].index(min(matrix[0])))
    Prim(matrix, 0)




if __name__ == "__main__":
    main()