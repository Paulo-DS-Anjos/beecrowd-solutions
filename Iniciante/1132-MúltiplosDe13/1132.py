# -*- coding: utf-8 -*-
x = int(input())
y = int(input())
if x > y:
    x,y=y,x
cont = 0
for i in range (x,y+1,1):
    if i % 13 != 0:
        cont += i
print(cont)  