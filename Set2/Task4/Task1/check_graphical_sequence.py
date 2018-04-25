def calculateSequence(sequence):

    #usuwać zera
    #sortować
    #brać pierwszy element
    #jeżeli lista zostanie pusta(same zera) to true
    #jeżeli zostanie jeden niezerowy element to nie jest ciągiem graficznym
    #jeżeli wyjdzie poza zakres listy przy odejmowaniu, np ciąg 4 3 to też fałsz

    while(len(sequence)>1):
        sequence = sorted(sequence, reverse=True)


        while 0 in sequence:#usuń zera z listy
            sequence.remove(0)


        if (len(sequence) == 0):
            return True

        edge_nmb = sequence[0]
        sequence[0] = 0


        cur_vertex = 1
        while (edge_nmb > 0):
            if (cur_vertex >= len(sequence)):
                return False  # nie jest graficzny, wyszlo poza zakres//

            sequence[cur_vertex] -= 1
            cur_vertex += 1  # przejscie do kolejnego wierzcholka
            edge_nmb -= 1  # zmniejszona liczba polaczen


    return False


if __name__  == "__main__":
    sequence = [ int(x) for x in input().split()]

    print(sequence)

    if calculateSequence(sequence):
        print("Jest ciagiem graficznym")
    else:
        print("Nie jest ciagiem graficznym")
