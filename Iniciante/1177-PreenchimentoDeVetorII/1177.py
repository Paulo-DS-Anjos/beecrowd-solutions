# -*- coding: utf-8 -*-
t= int(input())
lista = []
for x in range (0,999,t):
    for y in range (t):
        if x <= 999:
            print(f'N[{x}] = {y}')
            x += 1