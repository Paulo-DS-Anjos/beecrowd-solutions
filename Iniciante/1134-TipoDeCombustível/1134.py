# -*- coding: utf-8 -*-
a = 0
g = 0
d = 0
while True:
    x = int(input())
    if x == 1:
        a += 1
    elif x == 2:
        g += 1
    elif x == 3:
        d += 1
    elif x == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {a}')
        print(f'Gasolina: {g}')
        print(f'Diesel: {d}')
        break