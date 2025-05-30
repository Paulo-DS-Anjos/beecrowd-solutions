# 1099 - Soma de Ímpares Consecutivos II

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1099)

Leia um valor inteiro ``N`` que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros ``X`` e ``Y``. Você deve apresentar a soma de todos os ímpares existentes entre ``X`` e ``Y``.

### Entrada:
A primeira linha de entrada é um inteiro ``N`` que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros ``X`` e ``Y``.

### Saída:
Imprima a soma de todos valores ímpares entre ``X`` e ``Y``.

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
|          7          |         0         |
|         4 5         |        11         |
|        13 10        |         5         |
|         6 4         |         0         |
|         3 3         |         0         |
|         3 5         |         0         |
|         3 4         |         0         |
|         3 8         |        12         |

## Solução

Vide problema [1071 - Soma de Ímpares Consecutivos I](1071-SomaDeÍmparesConsecutivosI).

## Python 3.9

```Python
# -*- coding: utf-8 -*-
N= int(input())
for _ in range(N):
    X, Y = map(int, input().split())

    if X > Y:
        X, Y = Y, X

    soma_impares = 0

    for num in range(X + 1, Y):
        if num % 2 != 0:
            soma_impares += num

    print(soma_impares)  
```