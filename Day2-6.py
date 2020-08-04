# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:47:55 2020

@author: USER
"""
scr=[]
s=[]
total=0
avg=0

n=input("輸入人數:")
n=int(n)
for x in range(n):
    scores=input("輸入分數:")
    scores = int(scores)
    scr.append(scores)
    names=input("輸入名字:")
    s.append(names)
    total = total + scr(x)
print(scr)
    #total = total + scr()
print(total)

    
