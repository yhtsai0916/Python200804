# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:22:49 2020

@author: USER
"""

x=input("輸入數字:")
x=int(x)
i=0
while i<(x-2):
    if x%(i+2)==0:
        print("不是質數")
i=i+1
print("是質數")