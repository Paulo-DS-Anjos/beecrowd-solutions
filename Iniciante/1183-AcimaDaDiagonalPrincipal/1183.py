# -*- coding: utf-8 -*-
O = input()
MATRIZ = [[0.0 for _ in range(12)] for _ in range(12)]

for linha in range(12):
    for coluna in range(12):
        MATRIZ[linha][coluna] = float(input())

soma = 0.0
contador = 0

for linha in range(12):
    for coluna in range(12):
        if linha < coluna:
            soma += MATRIZ[linha][coluna]
            contador += 1

if O == 'S':
    print(f"{soma:.1f}")
else:
    print(f"{soma / contador:.1f}")
