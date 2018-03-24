# Matrix Conversion

Program odpowiedzialny za konwersje macierzy. Obsługuje 3 rodzaje macierzy:
* Macierz Sąsiedztwa (MS)
* Lista Sąsiedztwa (LS)
* Macierz Incydencji (MI)

Program rozpoznaje typ reprezentacji grafu poprzez podanie, któregoś z trzech skrótów podanych w nawiasach. Graf musi być przechowywane w pliku graph_in.txt

Sposób zapisu grafów jest pokazany poniżej. Każda reprezentacja przedstawia identyczny graf:

MS:
```
MS
0 1 0 0 1
1 0 1 1 1
0 1 0 1 0
0 1 1 0 1
1 1 0 1 0
```
LS:
```
LS
2 5
1 3 4 5
2 4
2 3 5
1 2 4
```
MI: (każda krawędź to osoby wiersz a kolumna to wierzchołek)
```
MI
1 1 0 0 0
1 0 0 0 1
0 1 1 0 0
0 1 0 1 0
0 1 0 0 1
0 0 1 1 0
0 0 0 1 1
```

Autor: Paweł Oczadly (kiedyś tam w marcu)
