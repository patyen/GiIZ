Zestaw 1, zadanie 1 - generowanie grafow 

Prosty skrypt do losowania grafow.

Użycie:
a) Podajac prawdopodobienstwo z ktorym krawedzie beda ze soba polaczone:
    Format: python3 random_graphs.py p prawdopodobienstwo_w_zakresie_[0, 1] liczba_wierzcholkow

    Przyklad: python3 random_graphs.py p 0.5 10

b) Podajac liczbe krawedzi:
    Format: python3 random_graphs.py l liczba_krawedzi liczba_wierzcholkow

    Przyklad: python3 random_graphs.py l 5 30

Wygenerowany graf moze byc niespojny.


Output:
Plik zawiera macierz incydencji

Przykladowy output w pliku graph.txt