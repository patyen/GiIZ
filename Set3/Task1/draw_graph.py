import numpy as np
import math as m
import matplotlib.pyplot as plt
import sys
file = open(sys.argv[1], "r")

data = [i.split() for i in file  if i != 'MI\n']
r = 1
x = []
y = []
text_x = []
text_y = []

#calculating points coordinances
for i in range(len(data[0])):
    alfa = 2 * m.pi * i / len(data[0])
    x.append(r * m.cos(alfa))
    y.append(r * m.sin(alfa))
    text_x.append(1.2*r * m.cos(alfa))
    text_y.append(1.2*r * m.sin(alfa))

x = np.array(x)
y = np.array(y)

#calculating lines
lines=[]
for record in data:
    xs = []
    ys = []
    for i, el in enumerate(record):
        if el == '1':
            xs.append(x[i])
            ys.append(y[i])
    plt.plot(xs,ys, c='b')
print(lines)

#plotting
plt.scatter(x,y, c='r')
plt.axis('off')
for i in range(len(x)):
    plt.text(text_x[i],text_y[i], str(i+1))
plt.show()
