# -*- coding: utf-8 -*-
vetor = []
for _ in range(100):
    vetor.append(float(input()))
for i in range(len(vetor)):
  if vetor[i] < 11:
    print(f'A[{i}] = {vetor[i]}')