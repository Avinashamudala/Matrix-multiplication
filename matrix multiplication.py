# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=[[1,2,7],
   [3,4,8],
   [9,7,0]]
b=[[4,3,3],
   [2,1,7],
   [6,8,2]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]]
x=input("number of rows in matrix 1 : ")
y=input("number of coloumns in matrix 2 : ")
if x==y
 for i in range(0,len(a)):
   for j in range(0,len(b)):
       c[i][j]=0
       for k in range(0,len(a)):
              c[i][j] = c[i][j] + (a[i][k]*b[k][j])
else print("multiplication cannot be done")
print(c)