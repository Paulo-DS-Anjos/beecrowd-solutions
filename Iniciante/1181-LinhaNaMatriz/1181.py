# -*- coding: utf-8 -*-
L = int(input())
T = input()
MATRIZ = [[0.0 for _ in range(12)]for _ in range(12)]

for linha in range(12):
    for coluna in range(12):
        MATRIZ[linha][coluna] = float(input())

if T == "S":
    print(f"{sum(MATRIZ[L]):.1f}")
else:
    print(f"{sum(MATRIZ[L])/12:.1f}")