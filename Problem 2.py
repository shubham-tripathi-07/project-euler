#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:21:54 2022

@author: apple
"""
a,b,c,add,n = 1,1,0,0,0
while n <= 4000000:
    c = a+b
    a = b
    b = c
    if c%2 == 0:add += c
    n = c
print(add)    
    
    
