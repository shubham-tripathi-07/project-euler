#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:09:03 2022

@author: apple

Problem Statement: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
largest_palindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = str(i*j)
        if product[::-1] == product and int(product) > largest_palindrome:
            largest_palindrome = int(product)
print(largest_palindrome)            
            
            
