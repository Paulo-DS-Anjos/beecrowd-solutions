# -*- coding: utf-8 -*-
n = int(input())
for _ in range (n):
    x,y = map(int,input().split())
    soma = 0
    if x % 2 == 0:
        x += 1
    for i in range (y):
        soma += x
        x+= 2
    print(soma)