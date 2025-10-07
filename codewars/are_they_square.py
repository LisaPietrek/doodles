#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
kata from www.codewars.com

title: Are they square? 7kyu

Desecription: 
Write a function that checks whether all elements in an array are square numbers. The function should be able to take any number of array elements.

Your function should return true if all elements in the array are square numbers and false if not.

An empty array should return undefined / None / nil /false (for C). You can assume that all array elements will be positive integers.

Examples:

is_square([1, 4, 9, 16]) --> True

is_square([3, 4, 7, 9]) --> False

is_square([]) --> None

"""

def s(i):
    # Babylonian algorithm for square root
    x = i // 2
    l = [x]
    while x * x != i and x != 0 :
        x = (x + (i // x)) // 2
        if x in l: return False
        l.append(x)
    return True

def is_square(arr):
    if not arr == []:
        checks = set(map(s, arr))
        if checks.__len__() == 2:
            return False
        return checks.pop()
        
    return None
