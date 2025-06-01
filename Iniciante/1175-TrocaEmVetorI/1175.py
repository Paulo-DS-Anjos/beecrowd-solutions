# -*- coding: utf-8 -*-
vetor = []
for i in range(20):
  vetor.append(int(input()))
x = 0
y = 19
while x <= 9:
  vetor[x],vetor[y]=vetor[y],vetor[x]
  x += 1
  y -= 1
for i in range(len(vetor)):
  print(f'N[{i}] = {vetor[i]}')