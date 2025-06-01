# -*- coding: utf-8 -*-
s = 0
j = 1
for i in range (1,39+1,2):
    s += (i/j)
    j += j
print(f'{s:.2f}')