# -*- coding: utf-8 -*-
OPERACAO = input()
MATRIZ = [[0.0 for _ in range(12)]for _ in range(12)]

for LINHA in range(12):
    for COLUNA in range(12):
        MATRIZ[LINHA][COLUNA] = float(input())

SOMA = 0.0
INICIO = 1
FIM = 10
for LINHA in range(0,5):
    for COLUNA in range(INICIO,FIM+1):
        SOMA += MATRIZ[LINHA][COLUNA]
    INICIO += 1
    FIM -= 1
        
if OPERACAO == "S":
    print(f"{SOMA:.1f}")
else:
    print(f"{SOMA/30:.1f}")