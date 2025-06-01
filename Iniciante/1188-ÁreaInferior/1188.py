# -*- coding: utf-8 -*-
OPERACAO = input()
MATRIZ = [[0.0 for _ in range(12)]for _ in range(12)]

for LINHA in range(12):
    for COLUNA in range(12):
        MATRIZ[LINHA][COLUNA] = float(input())

SOMA = 0.0
for LINHA in range(12):
    for COLUNA in range(12):
        if LINHA > COLUNA and LINHA + COLUNA > 11:
            SOMA += MATRIZ[LINHA][COLUNA]
            
if OPERACAO == "S":
    print(f"{SOMA:.1f}")
else:
    print(f"{SOMA/30:.1f}")