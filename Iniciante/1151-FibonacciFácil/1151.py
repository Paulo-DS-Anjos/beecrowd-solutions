# -*- coding: utf-8 -*-
x = int(input())
lista = [0,1]
for i in range(2,x):
    proximo = lista[i-1] + lista[i-2]
    lista.append(proximo)
print(' '.join(map(str,lista[:x])))