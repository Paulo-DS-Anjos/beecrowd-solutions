# -*- coding: utf-8 -*-
n = int(input())
fatorial = n
for n in range (n -1,0,-1):
    fatorial *= n
print(fatorial)