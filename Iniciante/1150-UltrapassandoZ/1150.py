# -*- coding: utf-8 -*-
X = int(input())
while True:
    Z = int(input())
    if Z > X:
        break
soma = 0
contador = 0
valor_atual = X
while soma <= Z:
    soma += valor_atual
    valor_atual += 1
    contador += 1
print(contador)