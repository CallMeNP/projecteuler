#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""
import json
import itertools
import math


def is_square_num(num):
    return int(num ** 0.5) ** 2 == num


def trans_word2num(w, char2num):
    n = 0
    for c in w:
        n = n * 10 + int(char2num[c])
    return n


def check_pairs(w1, w2):
    sw = "".join(sorted(list(set(w1))))
    l = len(sw)
    for i in itertools.permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], l):
        c2n = dict(zip(sw, i))
        n1 = trans_word2num(w1, c2n)
        n2 = trans_word2num(w2, c2n)
        if is_square_num(n1) and is_square_num(n2):
            if math.floor(math.log10(n1)) == math.floor(math.log10(n2)):
                print(n1, w1, n2, w2)
                return n1, n2
    return 0, 0


data_file = open("./p098_words.txt")

data_str = data_file.readline()
data_str = "[" + data_str + "]"
data = json.JSONDecoder().decode(data_str)  # type:list
dic = dict()
pairs = []
for w in data:
    sw = "".join(sorted(w))
    if sw in dic:
        dic[sw].append(w)
    else:
        dic[sw] = [w]
    if len(dic[sw]) > 1:
        print(dic[sw])
        pairs.append(dic[sw])
print(len(pairs))

square_nums = []
for p in pairs:
    n1, n2 = check_pairs(p[0], p[1])
    if n1:
        square_nums.append(n1)
        square_nums.append(n2)

print(max(square_nums))
print(sorted(square_nums))
