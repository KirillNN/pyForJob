# pip install matplotlib
from pylab import *
import random

x = linspace(0, 5, 10)
y = x ** 2
# print(x,y)
x = [0, 1, 2]
y = [0, 1, 4]

count_random = dict()

for ff in range(1000000000):
    i = random.randint(1, 10)
    if i in count_random:
        count_random[i] += 1
    else:
        count_random[i] = 1
    if ff % 1000000 == 0:
        print(round(ff/1000000))
    # print(random.randint(1, 10))

print(count_random)

# my_dict = { 'Khan': 4, 'Ali': 2, 'Luna': 6, 'Mark': 11, 'Pooja': 8, 'Sara': 1}

myList = count_random.items()
myList = sorted(myList)
x, y = zip(*myList)

figure()
plot(x, y, 'r')
grid()
xlabel('x')
ylabel('y')
title('Распределение случайных чисел')
show()
