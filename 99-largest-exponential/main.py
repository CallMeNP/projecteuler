#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import math

data_file = open("./p099_base_exp.txt", "r")
data = data_file.readlines()

values = []
for i in range(len(data)):
    row = data[i]
    nums = row.split(",")
    v = math.log(float(nums[0]))*float(nums[1])
    values.append((v, i+1, row))

values.sort()
print(values[-1])
