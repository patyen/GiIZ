#Check Graphical Sequence

Program sprawdza czy podana przez użytkownika sekwencja jest sekwencją graficzną.
Nie sprawdza on czy suma wszystkich wyrazów w sekwencji jest parzysta czy też któryś ze stopni wierzchołka jest większy lub równy liczby wierzchołków w sekwencji.
Program wyświetla sekwencje w trakcie wykonywania algorytmu co pozwala na jego prześledzenie.
W skrócie wygląda ona następująco:

* dopóki w liście więcej niż jeden element
+ posortuj listę malejąco
+ usuń elementy równe zero
+ jeśli lista jest pusta to zwróć true (ciąg jest graficzny)
+ w przeciwnym razie wyzeruj pierwszy element i zapamiętaj jego wartość(m). Następnie odejmuj jeden od kolejnych wyrazów sekwencji. Jeśli wyjdzie poza zakres listy to false.

Jeśli po wyjściu z pętli lista jest niepusta to oznacza, że pozostał w niej element niezerowy i ciąg nie jest graficzny, czyli false.

Autor: Paweł Oczadly (kiedyś tam w marcu)
