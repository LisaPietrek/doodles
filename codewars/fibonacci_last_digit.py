#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
kata from www.codewars.com

title: Find fibonacci last digit. 7kyu
Desecription:
As you probably know, Fibonacci sequence are the numbers in the following integer sequence: 1, 1, 2, 3, 5, 8, 13... Write a method that takes the index as an argument and returns last digit from fibonacci number. Example: getLastDigit(15) - 610. Your method must return 0 because the last digit of 610 is 0. Fibonacci sequence grows very fast and value can take very big numbers (bigger than integer type can contain), so, please, be careful with overflow.

"""

def fib(n):
    a, b = 0, 1
    l = []
    for i in range(n):
        a, b = b, a+b
        l.append(a)
        
    return l
    
def get_last_digit(index):
    l = fib(index)
    return l[-1] % 10
