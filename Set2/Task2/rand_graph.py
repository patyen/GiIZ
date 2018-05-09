import random
import sys

file = open(sys.argv[1], "r")

data = [i.split() for i in file  if i != 'MI\n']

flag = 1
data_size = len(data)
if(data_size) > 2:
    while flag:
        first_index = random.choice(range(len(data)))
        second_index = random.choice(range(len(data)))
        while first_index == second_index:
            second_index = random.choice(range(len(data)))

        tmp1 = data[first_index]
        tmp2 = data[second_index]

        back1 = tmp1[:]
        back2 = tmp2[:]
        
        if(first_index < second_index):
            data.pop(second_index)
            data.pop(first_index)
        else:
            data.pop(first_index)
            data.pop(second_index)
    
        zipped = zip(tmp1, tmp2)
        flag = 0
        if ('1','1') in zipped:
            flag = 1

        n_index_one = tmp1.index('1')
        n_index_two = tmp2.index('1')

        tmp1[n_index_one] = '0'
        tmp2[n_index_two] = '0'
        
        tmp1[n_index_two] = '1'
        tmp2[n_index_one] = '1'

        if tmp1 in data or tmp2 in data:
            flag = 1
            data.append(back1)
            data.append(back2)
                    
data.append(tmp1)
data.append(tmp2)

tosave = open("result.txt",'w')

tosave.write('MI\n')
for el in data:
    for i, num  in enumerate(el):
        tosave.write(str(num))
        if i != len(el) - 1:
            tosave.write(' ')
    tosave.write('\n')
