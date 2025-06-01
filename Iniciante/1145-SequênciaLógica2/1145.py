# -*- coding: utf-8 -*-
X,Y = map(int,input().split())
for i in range(1, Y + 1):
    print(i, end="")
    if i % X == 0:
        print()
    else:
        print(" ", end="")