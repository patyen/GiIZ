# generowanie spójnych grafów ważonych

Program oparty o rozwiązanie z pierwszego zestawu

Użycie:
a) Podajac prawdopodobienstwo z ktorym krawedzie beda ze soba polaczone:
    Format: python3 random_graphs.py p prawdopodobienstwo_w_zakresie_[0, 1] liczba_wierzcholkow

    Przyklad: python3 random_graphs.py p 0.5 10

b) Podajac liczbe krawedzi:
    Format: python3 random_graphs.py l liczba_krawedzi liczba_wierzcholkow

    Przyklad: python3 random_graphs.py l 5 30


Wybierając opcję z prawdopodobieństwem możliwe jest wygenerowanie grafu nie posiadającego wystarczającej liczby krawędzi, wtedy konieczne jest ponowne uruchomienie skryptu.


Output:
Plik zawiera macierz incydencji, bez podanych wag w celu rysowania( matrix.out)
Oraz plik zawierający ważoną macierz sąsiedztwa( graph.out )

Przykladowy output w pliku graph.out


Autor: Paweł Oczadly - dodanie opcji tworzenia grafów spójnych i ważonych, modyfikacja wcześniejszych rozwiązań (kiedyś tam w maju)
Patryk Nguyen - wcześniejsza wersja
Daniel Piskorski - wykorzystany program do zamiany krawędzi
	
