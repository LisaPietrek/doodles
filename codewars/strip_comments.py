#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
kata from www.codewars.com

title: Strip Comments. 4kyu

Desecription:
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas
"""

def strip_comments(strng, markers):
    
    x = strng.split("\n")
#     print(x)
    a=[]
    for ii in x:
#         print(ii)
        for m in markers:
            i = ii.find(m)
            if i != -1:
                ii = ii[:i]
        a.append(ii.rstrip(" "))
#     print(a)
    return "\n".join(a) 
