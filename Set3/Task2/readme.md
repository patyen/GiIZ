# Dijkstra

Program wykonujący algorytm Dijkstry dla grafu prostego, w których przyporządkowano każdej krawędzi odpowiednią wagę.
Opis algorytmu, który zaimplementowano w niniejszym programie znajduje się w Cormenie ,,Wprowadzenie do algorytmów" - przykład można znaleźć tutaj http://home.agh.edu.pl/~ewach/grafy/najkrotsza.pdf
Program wybiera jako wierzchołek startowy wierzchołek nr 1(pierwszy wiersz w macierzy)

Graf przetwarzany przez program powinien się znajdować w pliku ```graph_in.txt``` i być w następującym formacie(poniżej jest zaprezentowany ten sam graf co na laboratorium i w przykładowym pliku graph_in.txt).
Przykładowo w drugim wierszu i w pierwszej kolumnie macierzy, wartość 2 oznacza wagę krawędzi łączącej wierzchołek 1 i 2. Wartość 0 oznacza, że wierzchołki nie są połączone. Jako, że zakładamy, że operujemy na grafach prostych, to macierz jest symetryczna.
```
0 2 0 0 0 0 4
2 0 8 0 0 4 1
0 8 0 1 5 4 0
0 0 1 0 3 0 0
0 0 5 3 0 7 0
0 4 4 0 7 0 2
4 1 0 0 0 2 0
```

Autor: Paweł Oczadly (kiedyś tam w marcu)
