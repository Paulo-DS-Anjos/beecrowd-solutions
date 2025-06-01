# -*- coding: utf-8 -*-
lista = []
x = -1
while x != 0:
    x = int(input())
    if x == 0:
        break
    else:
        lista.append(x)
for i in lista:
    for j in range(1,i+1):
        if j == i:
            print(j , end='')
        else:
            print(j , end=' ')
    print('')