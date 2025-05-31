# -*- coding: utf-8 -*-
C = int(input())
T = input()
MATRIZ = [[0.0 for _ in range(12)] for _ in range(12)]

for linha in range(12):
    for coluna in range(12):
        MATRIZ[linha][coluna] = float(input())
X = 0
for linha in range(12):
    X += MATRIZ[linha][C]
if T == "S":
    print(f"{X:.1f}")
else:
    print(f"{(X/12):.1f}")