# -*- coding: utf-8 -*-
T = int(input())
for i in range(T):
    T = int(input())
    if T == 0:
        print("Fib(0) = 0")
    elif T == 1:
        print("Fib(1) = 1")
    else:
        fib = [0, 1]
        for j in range(2, T + 1):
            J_fib = fib[j - 1] + fib[j - 2]
            fib.append(J_fib)
        print(f"Fib({T}) = {fib[T]}")