#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
https://projecteuler.net/problem=54

1.High Card: Highest value card.
2.One Pair: Two cards of the same value.
3.Two Pairs: Two different pairs.
4.Three of a Kind: Three cards of the same value.
5.Straight: All cards are consecutive values.
6.Flush: All cards of the same suit.
7.Full House: Three of a kind and a pair.
8.Four of a Kind: Four cards of the same value.
9.Straight Flush: All cards are consecutive values of same suit.
10.Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""


class Card:
    def __init__(self, str):
        """
        :type str: str
        """
        if len(str) != 2 or str[0] not in "23456789TJQKA" or str[1] not in "CSHD":
            raise Exception("bad card")
        self.value = str[0]
        if self.value.isdigit():
            self.order = int(self.value)
        elif self.value.isalpha():
            self.order = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}[self.value]
        self.suit = str[1]

    def __cmp__(self, other):
        """
        :type other: card
        :return: int
        """
        return cmp(self.order, other.order)


class Hand:
    def __init__(self, str):
        """
        
        :type str: str
        """
        if len(str) < 14:
            raise Exception("bad hand: bad str")
        cards = str.split(" ")
        if len(cards) < 5:
            raise Exception("bad hand: bad card num")
        self.cards = [Card(i) for i in cards]
        self.cards.sort()
        self.count = self.card_count()

    def __cmp__(self, other):
        """
        :type other: Hand
        :return: 
        """
        self_match_rule = self.match_rule()
        other_match_rule = other.match_rule()
        if self_match_rule != other_match_rule:
            return cmp(self_match_rule, other_match_rule)
        if self_match_rule == 10:
            raise Exception("undefined situation:both royal flush")
        if self_match_rule in [1, 2, 3, 5, 9, 4, 7, 8, 6]:
            s = sorted(zip(self.count.values(), self.count.keys()), reverse=True)
            o = sorted(zip(other.count.values(), other.count.keys()), reverse=True)
            print self_match_rule, s, o, "P1W" if cmp(s, o) >= 0 else "P2W"
            return cmp(s, o)
        # if self_match_rule in [5, 9]:
        #     s = self.get_highest_value()
        #     o = other.get_highest_value()
        #     print self_match_rule, s, o, "P1W" if cmp(s, o) >= 0 else "P2W"
        #     return cmp(s, o)
        # if self_match_rule in [1, 6]:
        #     s = sorted([x.order for x in self.cards], reverse=True)
        #     o = sorted([x.order for x in other.cards], reverse=True)
        #     print self_match_rule, s, o, "P1W" if cmp(s, o) >= 0 else "P2W"
        #     return cmp(s, o)
        raise Exception("undefined situation: bad rule match")

    def get_highest_value(self):
        """
        for rule 1
        :return: 
        """
        return max([x.order for x in self.cards])

    def is_straight(self):
        for i in range(1, len(self.cards)):
            if self.cards[i - 1].order + 1 != self.cards[i].order:
                return False
        return True

    def is_flush(self):
        return len(set([x.suit for x in self.cards])) == 1

    def is_royal(self):
        return set([x.value for x in self.cards]) == {"T", "J", "Q", "K", "A"}

    def match_rule(self):
        count_vlist = sorted(self.count.values())
        if self.is_royal() and self.is_flush():
            return 10
        elif self.is_straight() and self.is_flush():
            return 9
        elif count_vlist == [1, 4]:
            return 8
        elif count_vlist == [2, 3]:
            return 7
        elif self.is_flush():
            return 6
        elif self.is_straight():
            return 5
        elif count_vlist == [1, 1, 3]:
            return 4
        elif count_vlist == [1, 2, 2]:
            return 3
        elif count_vlist == [1, 1, 1, 2]:
            return 2
        return 1

    def card_count(self):
        count = dict()
        for i in self.cards:
            if i.order in count:
                count[i.order] += 1
            else:
                count[i.order] = 1
        return count


def build2hands(str):
    """
    :type str: str
    :return: 
    """
    if len(str) < 30:
        raise Exception("bad line")
    h1 = Hand(str[:14])
    h2 = Hand(str[15:29])
    return h1, h2


if __name__ == '__main__':
    f = open("./p054_poker.txt", "r")
    lines = f.readlines()
    c = 0
    for l in lines:
        h1, h2 = build2hands(l)
        if h1 > h2:
            c += 1
    print c
