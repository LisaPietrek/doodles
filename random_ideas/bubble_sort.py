#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple implementatiom of a bubble sort algorithm. 
For each element i in the array check if i is larger than its right
neighbor, if so, swap. Go to the next element (i=i+1) and repeat. 
Continue for the whole length of the array.

Bad time complexity, since it checks if i > j each round, 
regardless if they are already sorted. Suitable only for small arrays.
"""

def bubble_sort(arr):
    for num in range(len(arr)):
        i = 0
        j = 1
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
            
    return arr 

arr = [5, 1, 4 ,2, 8]
bubble_sort(arr)