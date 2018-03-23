from sys import argv



def next_nb(ls, visited, iterator, element):
    for i in range(len(ls[iterator])):
        print(f"{visited} {ls[iterator][i]}")
        if  visited[ls[iterator][i] - 1] == 0:
            visited[ls[iterator][i] - 1] = element
            next_nb(ls, visited, ls[iterator][i] - 1, element)




if len(argv) < 2:
    print("Podaj input")
    exit()


ls = []
visited = []
vertices = 0

# read graph from file
with open(argv[1]) as f:
    line = (str(f.readline()).rstrip())
    if line != "LS":
        print("Podaj liste sasiedztwa")
    for line in f:
        ls.append(line.rstrip().split(' '))
        vertices += 1

for i in range(len(ls)):
    if len(ls[i]) > 0 and ls[i][0] != '':
        ls[i] = list(map(int, ls[i]))
    else:
        ls[i].remove('')
f.close()

    


# set visited list to work
for i in range(vertices):
    visited.append(0)
# print(vertices)


element = 1
i = 0

for i in range(len(visited)):
    if visited[i] == 0:
        visited[i] = element
        next_nb(ls, visited, i, element)
    else:
        if element in visited:
            element += 1
    i += 1

print(ls)
#print(visited)
