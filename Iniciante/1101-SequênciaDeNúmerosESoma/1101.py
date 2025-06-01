# -*- coding: utf-8 -*-
while True:
    lista = []
    M,N = map(int,input().split())
    if M > N:
        M,N = N,M
    if (M <= 0):
        break
    for i in range(M,N+1):
        lista.append(i)
    print(f"{' '.join(map(str, lista))} Sum={sum(lista)}")