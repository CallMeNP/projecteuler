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
# ceiling(log(10,y^n))=n  ,  y=0,9
count=[]
for y in range(1,10):
    for n in range(1,100):
        power=y**n
        ceil_log10=len(str(power))
        if ceil_log10==n:
            print(y,n,power,len(str(power)))
            count.append(power)
            continue
        if ceil_log10>n:
            break

print(len(count))
