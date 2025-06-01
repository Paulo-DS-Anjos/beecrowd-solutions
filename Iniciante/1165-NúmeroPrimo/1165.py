# -*- coding: utf-8 -*-
N = int(input())
for _ in range(N):
  primo = True
  X = int(input())
  for i in range(2, X):
    if X % i == 0:
      primo = False
  if primo == True:
    print(f'{X} eh primo')
  else:
    print(f'{X} nao eh primo')