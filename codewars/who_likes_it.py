#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
kata from www.codewars.com

title: Who likes it? 6kyu

Desecription: 
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. We want to 
create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people 
that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.

"""


def likes(names):
    # prepare dictionary with all possible scenarios
    dict = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        # for all cases where four or more like the post
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    # find the matching key for dict > depends on the kength of 'names'
    # if length > 4, we resort to 4 as largest possible key in dict
    key = min(4, length)
    # use format on dict value to fill in the names and number of others
    # possible, since format ignores additional values, if all gaps in string are filled in
    return dict[key].format(*names, others = length-2)
