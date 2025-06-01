# -*- coding: utf-8 -*-
x = -1
while x != 2:
    nota1 = float(input())
    while (nota1 < 1 or nota1 > 10):
        print('nota invalida')
        nota1 = float(input())

    nota2 = float(input())
    while (1 > nota2 or nota2 > 10):
        print('nota invalida')
        nota2 = float(input())

    print(f'media = {(nota1 + nota2) / 2:.2f}')

    y = 0
    while y != 1 and y != 2:
        print('novo calculo (1-sim 2-nao)')
        y = int(input())
    if y == 2:
        break