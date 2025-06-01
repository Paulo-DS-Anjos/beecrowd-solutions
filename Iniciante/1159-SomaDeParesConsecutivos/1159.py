# -*- coding: utf-8 -*-
x = int(input())
j = 0
while x != 0:
    if x % 2 == 0:
      for i in range (x,x+9,2):
        j += i
      print(j)
    else:
      x += 1
      for i in range (x,x+9,2):
        j += i
      print(j)
    j = 0
    x = int(input())