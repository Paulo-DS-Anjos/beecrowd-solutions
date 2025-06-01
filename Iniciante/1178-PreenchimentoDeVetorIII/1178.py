# -*- coding: utf-8 -*-
VETOR = []
VETOR.append(float(input()))
for i in range(100):
    print(f"N[{i}] = {VETOR[-1]:.4f}")
    VETOR.append(VETOR[-1]/2)   