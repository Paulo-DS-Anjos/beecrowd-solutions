# -*- coding: utf-8 -*-
N = int(input())
for _ in range(N):
  X = int(input())
  soma = []
  for i in range(1,X):
    if X % i == 0:
      soma.append(i)
  if (sum(soma)) == X:
    print(f'{X} eh perfeito')
  else:
    print(f'{X} nao eh perfeito')