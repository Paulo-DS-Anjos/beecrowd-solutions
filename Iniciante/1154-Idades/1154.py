# -*- coding: utf-8 -*-
lista = []
media = 0
while True:
    x = int(input())
    if x >= 0:
        lista.append(x)
    else:
        break
media = sum(lista)/ len(lista)
print(f'{media:.2f}')