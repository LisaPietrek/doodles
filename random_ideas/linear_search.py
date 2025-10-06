#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple implementation of linear search algorithms
"""

def linear_search_one_sided(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1 # element not in arr


def linear_search_two_sided(arr, element):
    l = 0
    r = len(arr) - 1
    i = 1
    while i <= len(arr):
        if arr[l] == element:
            return l
        elif arr[r] == element:
            return r
        l += 1
        r -+ 1
        i += 1
    return -1 # element not in arr



arr = [1, 2, 3, 4, 5]
search_element = 5
linear_search_two_sided(arr, search_element)