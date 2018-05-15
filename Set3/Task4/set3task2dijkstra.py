def smallestDNotIncluded(S, d, weight_limit):
    min_value = weight_limit
    min_index = -1
    for i in range(len(d)):
        if i not in S and d[i] < min_value:
            min_value = d[i]
            min_index = i

    return min_index


def dijkstra(matrix, vertex):

    vertices_nmb = len(matrix)

    #init
    weight_limit = 0#odpowiednik nieskończoności
    for row in matrix:
        for weight in row:
            weight_limit += weight

    d = [weight_limit] * vertices_nmb #inicjalizuje poczatkowe odleglosci
    p = [-1] * vertices_nmb #wcześciejszy wierzchołek
    d[vertex] = 0 #startowy wierzcholek (wierzcholek 1) zerowany

    S=[]#zbior gotowych wierzcholkow


    while(len(S) != vertices_nmb):
        min_vertice = smallestDNotIncluded(S, d, weight_limit)
        S.append(min_vertice)#krok 5.
        #sprawdzić sąsiadów
        for v in range(len(matrix[min_vertice])):
            if matrix[min_vertice][v] != 0 and v not in S:#jest sąsiadem bo istnieje krawędź o niezerowej wadze i nie jest w zbiorze gotowych wierzchołków
                if( d[v] > d[min_vertice] + matrix[min_vertice][v]):#relaksacja
                    d[v] = d[min_vertice] + matrix[min_vertice][v]
                    p[v] = min_vertice

    #print("d: ", d) #to jest dobrze
    #print("p: ", [ node + 1 for node in p]) #aby wyswietlic nr wezla a nie indeksu. 0 oznacza pkt startowy

    return d


def main():
    graph_in = open("graph_in.txt", "r")

    matrix = [ line.replace("\n", "").split(" ") for line in graph_in.readlines() ]
    
    #pozbywanie się pustych elementów
    for row in matrix:
        if '' in row:
            row.remove('')	

    #konwersja na int
    matrix = [ [int(i) for i in row ]  for row in matrix ]
    print(matrix)
    dijkstra(matrix)

if __name__ == "__main__":
    #main()
    pass
