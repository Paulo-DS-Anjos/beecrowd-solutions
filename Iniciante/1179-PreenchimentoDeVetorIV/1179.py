# -*- coding: utf-8 -*-
vetor_par=[]
vetor_impar=[]

def exibir(nome,vetor):
    for i in range(len(vetor)):
        print(f"{nome}[{i}] = {vetor[i]}")

for _ in range (15):
    x = int(input())

    if x % 2 == 0:
        vetor_par.append(x)
      
        if len(vetor_par)==5:
          exibir("par",vetor_par)
          vetor_par = []
    else:
        vetor_impar.append(x)

        if len(vetor_impar)==5:
          exibir("impar",vetor_impar)
          vetor_impar = []
exibir("impar", vetor_impar)
exibir("par", vetor_par)