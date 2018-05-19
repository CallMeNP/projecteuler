#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""

import itertools


class Find4DigitCyclic:
    def __init__(self):
        p3 = lambda n: n * (n + 1) / 2  # 44<n<141
        p4 = lambda n: n * n  # 31 < n < 101
        p5 = lambda n: n * (3 * n - 1) / 2  # 25 < n < 82
        p6 = lambda n: n * (2 * n - 1)  # 22 < n < 71
        p7 = lambda n: n * (5 * n - 3) / 2  # 20 < n < 64
        p8 = lambda n: n * (3 * n - 2)  # 18< n < 59
        p_list = [p3, p4, p5, p6, p7, p8]
        # 所有公式的字典的列表
        self.p_dicts = [self.build_dict(p) for p in p_list]
        # 用于存储字典列表的一个排列
        self.permutation = tuple()
        # 用于存放cyclic数的所有前缀
        self.cyclic = []

    def build_dict(self, p):
        """
        将一个公式的所有4为数生成一个字典
        前两位为key，所有可能的后两位组成的list为该key的value
        :type p: function
        :rtype: dict
        """
        dic = dict()
        for i in range(200):
            num = p(i)
            if num < 1000:
                continue
            if num > 10000:
                break
            prefix = int(num / 100)
            appendfix = int(num % 100)
            if prefix in dic.keys():
                dic[prefix].append(appendfix)
            else:
                dic[prefix] = [appendfix]
        return dic

    def gen_permutation(self):
        # 生成所有排列
        for p_permutation in itertools.permutations(self.p_dicts):
            # 选定一个排列
            self.permutation = p_permutation
            # 对一个排列中算法字典0的每一个前缀进行遍历
            for pre in self.permutation[0].keys():
                got_it = self.find_in_permutation(pre, 0)
                if got_it:
                    # 题目中说明了唯一性，所以找到后就退出
                    break
            if got_it:
                break

    def find_in_permutation(self, pre, pdi):
        """
        指定第pdi个字典中，pre这个key下，所有的app
        看这些app有没有在下一个字典中能作为pre的
        透传找到了，或返回没找到
        :type pre: int
        :type pdi: int
        :rtype: bool
        """
        if pre not in self.permutation[pdi].keys():
            # 如果pre不在指定的字典中，返回:没找到
            return False
        self.cyclic.append(pre)
        for app in self.permutation[pdi][pre]:
            if pdi == 5:
                # 当指定字典为5时，即最后一个字典了。
                # 此事第五字典的app应是第一字典的pre
                if app == self.cyclic[0]:
                    # print(set(self.cyclic))
                    # 找到了
                    return True
                continue
            elif app not in self.permutation[pdi + 1].keys():
                continue
            got_it = self.find_in_permutation(app, pdi + 1)
            if got_it:
                return True
        else:
            # 遍历了本pre所有的app，没有找到
            # pop本pre并返回没找到
            self.cyclic.pop()
        return False


if __name__ == '__main__':
    f = Find4DigitCyclic()
    f.gen_permutation()
    num = []
    print(f.cyclic)
    for i in range(6):
        if i == 5:
            num.append(int("%d%d" % (f.cyclic[i], f.cyclic[0])))
            break
        num.append(int("%d%d" % (f.cyclic[i], f.cyclic[i + 1])))
    print("the six numbers are :", num)
    print("anser is: ", sum(num))
