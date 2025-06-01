# -*- coding: utf-8 -*-
num = int(input())
vet = []
vet.append(num)
print(f'N[0] = {vet[0]}')
for i in range (9):
  num = num * 2
  vet.append(num)
  print(f'N[{i+1}] = {vet[i+1]}')