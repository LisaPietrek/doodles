#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
kata from www.codewars.com

title: Multiples of 3 or 5. 6kyu
Desecription:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If a number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)


"""

import numpy as np

def solution(number):
    l = np.arange(number)
    if number < 0 :
        return 0
    else:
        xl = [x for x in l[1:]  if (x%3 == 0 or x%5 == 0) ]
        return sum(xl)
