# -*- coding: utf-8 -*-
x = []
cont = 0
for _ in range (10):
  n = int(input())
  x.append(n)
for i in x:
  if i <= 0:
    i = 1
  print(f'X[{cont}] = {i}')
  cont += 1