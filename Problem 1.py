#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:21:54 2022

@author: apple
"""
sum_of_factors = 0
for i in range(1000):
    if i%3==0 or i%5 == 0:sum_of_factors += i
print(sum_of_factors)    


        
    