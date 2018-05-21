#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""
cube_dict = {0: []}
for i in range(10000):
    cube = i ** 3
    s = "".join(sorted(str(cube)))
    if s in cube_dict.keys():
        cube_dict[s].append(cube)
        if len(cube_dict[s]) >= 5:
            print(cube_dict[s], s, i)
            break
        if len(cube_dict[s]) >= 3:
            print(cube_dict[s], s, i)
            continue
    else:
        cube_dict[s] = [cube]



