from random import random
from time import perf_counter

Darts = 10000000
hits = 0

start = perf_counter()

for i in range(1,Darts+1):
    x , y = random() , random()
    dist = pow( x**2 + y**2 , 0.5)
    if dist <= 1:
        hits += 1
pi = (hits/Darts) * 4

print('pi的蒙特卡罗值为：{}'.format(pi) )
print('运行时间为：{}'.format(perf_counter()-start))
