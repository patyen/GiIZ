correct_matrix_types = ["MI", "LS", "MS"] #poprawne sposoby na zapis macierzy
#w MI każdy rząd to kolejna krawędź (odwrotnie niż w zeszycie)

class Matrix:
    _content = ""
    _type = ""

    def __init__(self, input, matrix_type):
        self._type = matrix_type
        self._content = [[int(vertex) for vertex in row] for row in input]

        #if( self._type != "MS" or self._type != "LI" or self._type != "LS"):
        if self._type not in correct_matrix_types:
            return None

    #na razie tylko pod MS
    def print_matrix(self):
        print( self._type )
        if( self._type == "MS" ):
            for row in self._content:
                print(*row)
        else:
            for vertex in range(len(self._content)):
                print( str(vertex + 1) + ".", *self._content[vertex] )

    def write_matrix_to_file(self):
        output = open("matrix.out", "w")


        print(self._type, file=output)
        if( self._type == "MS" ):
            for row in self._content:
                print(*row, file=output)
        else:
            for vertex in range(len(self._content)):
                print(*self._content[vertex], file=output)


    def convert_matrix(self, type_to_convert):
        if( self._type == type_to_convert ):
            return None

        #najpierw konwertuj do macierzy sąsiedztwa

        if( self._type == "MI"):
            nmb_of_vertex = len(self._content[0])

            #tmp = [[0] * nmb_of_vertex] * nmb_of_vertex #to rozwiązanie błedne, tworzy referencję a nie listę
            tmp = [0] * nmb_of_vertex

            for i in range(nmb_of_vertex):
                tmp[i] = [0] * nmb_of_vertex


            for vertex in self._content:
                column = vertex.index(1)#szuka jedynki
                row = vertex.index(1, column + 1)# szuka kolejnej jedynki
                tmp[column][row] = 1
                tmp[row][column] = 1
                    #szuka pozycji gdzie jedynki i wtedy [kolumna][rząd] [rząd][kolumna]
            self._content = tmp
        elif( self._type == "LS" ):
            tmp = []
            matrix_length = len(self._content)
            for vertex in self._content:
                    tmp.append([1 if neighbour + 1 in vertex else 0 for neighbour in range(matrix_length)])

            self._content = tmp

        #właściwa konwersja

        if( type_to_convert == "LS" ):
            #zewnętrzna część przechodzi po kolejnych elemntach list np. ['01001', '10111', '01010', '01101', '11010']
            #wewnętrzna przechodzi po stringu i jeżeli napotka 1 to zapisuje nr iteracji
            #self._content[:] = [ [ vertex + 1 for vertex in range(len(row)) if row[vertex]=='1' ]for row in self._content]
            self._content[:] = [ [ vertex + 1 for vertex in range(len(row)) if row[vertex] ]for row in self._content]
        elif( type_to_convert == "MI" ):
            #self._content[:] = [ [ 1 if self._type[row_nmb][col_nmb] else 0 for row_nmb in range(len(col_nmb), range(self._content)) ] for col_nmb in range(self._content)]
            tmp=[]
            matrix_length = len(self._content)

            for col_nmb in range(matrix_length):
                for row_nmb in range(col_nmb, matrix_length):
                    if( self._content[row_nmb][col_nmb]):#jeżeli znaleziono krawędź
                        tmp.append( [ 1 if (i == row_nmb or i == col_nmb) else 0 for i in range(matrix_length) ] )

            #podmiana na macierz incydencji
            self._content = tmp

        #przypisanie nowego typu
        self._type = type_to_convert










def main():
    f = open("graph_in.txt", "r")

    #sprawdzenie typu zapisu macierzy - ucina znak nowej linii z pobranej linkijki
    matrix_type = f.readline().replace("\n","")

    #tworzy nową listę przechowującą kolejne rzędy - przy okazji pozbywa się znaku nowej linii i spacji
    input_from_file = [ w.replace("\n","").replace(" ","") for w in f.readlines() ]

    new_matrix = Matrix(input_from_file, matrix_type)

    #w przypadku gdy podano nieprawidłowy typ macierzy w pierwszej linijce
    if( new_matrix == None ):
        print("Zaladowano niepoprawny typ macierzy")
        return -1

    print("Zaladowano macierz typu: ", matrix_type)

    new_matrix.write_matrix_to_file()

    '''

    #testowanie konwersji
    for matrix_type in correct_matrix_types:
        new_matrix.convert_matrix(matrix_type)
        new_matrix.print_matrix()
    '''
    what_type = input("Do jakiego typu macierzy chcesz dokonac konwersji?")

    print(what_type)

    if( what_type in correct_matrix_types ): #sprawdzenie poprawności typu
        if( what_type == new_matrix._type ):
            print("Konwersja nie jest potrzebna")
            return -2
        else:
            new_matrix.convert_matrix(what_type)
    else:
        print("Podano niepoprawny typ macierzy")
        return -1

    new_matrix.print_matrix()
    new_matrix.write_matrix_to_file()





if __name__ == "__main__":
    main()