# -*- coding: utf-8 -*-
N= int(input())
for _ in range(N):
    X, Y = map(int, input().split())

    if X > Y:
        X, Y = Y, X

    soma_impares = 0

    for num in range(X + 1, Y):
        if num % 2 != 0:
            soma_impares += num

    print(soma_impares) 