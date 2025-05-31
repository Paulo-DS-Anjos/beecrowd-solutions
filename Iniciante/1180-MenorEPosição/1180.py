# -*- coding: utf-8 -*-
input()
VETOR = list(map(int, input().split()))
for i in VETOR:
    if i == min(VETOR):
        print(f'Menor valor: {i}')
        print(f'Posicao: {VETOR.index(i)}')
        break