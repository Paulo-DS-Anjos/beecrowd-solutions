# -*- coding: utf-8 -*-
def determinar_quadrante(x, y):
    if x > 0 and y > 0:
        return "primeiro"
    elif x < 0 and y > 0:
        return "segundo"
    elif x < 0 and y < 0:
        return "terceiro"
    elif x > 0 and y < 0:
        return "quarto"

while True:
    coordenadas = input().split()
    x = int(coordenadas[0])
    y = int(coordenadas[1])
    if x == 0 or y == 0:
        break
    quadrante = determinar_quadrante(x, y)
    print(quadrante)