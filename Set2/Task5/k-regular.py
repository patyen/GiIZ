import sys
import random
import time

k = int(sys.argv[1]) #stopien wierzchołków
n = random.randint(k+1, 2*k) #liczba wierzchołków

while (k * n)%2:
    n = random.randint(k+1, 2*k)

vert = 0
bad = 1 #flaga okreslajaca czy aktualny graf nie spełnia warunków


while bad:
    numbers = [i % int(n*k/2) for i in range(k*n)]
    vertexes = [[] for i in range(n)]

#assigining connecting sections to vertexes
    for i in range(n*k):
        index = random.randint(0,n*k -i -1)
        b=2*n  #ograniczenie liczby obiegów pętli while
        while numbers[index] in vertexes[vert] and b !=0 :
            index = random.randint(0,n*k-i-1)
            b -= 1
        vertexes[vert].append(numbers.pop(index))
        vert += 1
        vert %= n

    #creating incidention matrix
    im = [[] for i in range(int(n*k/2))]
    for nu in range(len(im)):
        for i in range(len(vertexes)):
            if nu in vertexes[i]:
                im[nu].append(1)
            else:
                im[nu].append(0)
    #print(im)
    bad = 0
    #sprawdzamy czy grupowanie krawędzi z wierzchołkami sie nie udało
    if not b:
        bad = 1
    #sprawdzamy czy nie ma wielokrotnych połączeń między wierzchołkami
    for ar in im:
        cnt = 0
        for ar_s in im:
            if ar == ar_s:
                cnt += 1
        if cnt > 1:
            bad = 1

f = open("data.txt","w")
f.write("MI\n")
for ar in im:
    for n in ar:
        f.write("{} ".format(n))
    f.write("\n")
