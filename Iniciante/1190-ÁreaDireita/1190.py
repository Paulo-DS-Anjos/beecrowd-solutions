# -*- coding: utf-8 -*-
OPERACAO = input()
MATRIZ = []

for LINHA in range(12):
    LINHA_COLUNA = []
    for COLUNA in range(12):
        LINHA_COLUNA.append(float(input()))
    MATRIZ.append(LINHA_COLUNA)

SOMA = 0.0
for LINHA in range(12):
    for COLUNA in range(12):
        if COLUNA > LINHA and COLUNA > 11 - LINHA:
            SOMA += MATRIZ[LINHA][COLUNA]

if OPERACAO == "S":
    print(f"{SOMA:.1f}")
else:
    print(f"{SOMA/30:.1f}")