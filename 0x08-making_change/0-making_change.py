#!/usr/bin/python3
"""Making Change
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    remain = total
    number = 0
    index = 0
    sorting = sorted(coins, reverse=True)
    n = len(coins)
    while remain > 0:
        if index >= n:
            return -1
        if remain - sorting[index] >= 0:
            remain -= sorting[index]
            number += 1
        else:
            index += 1
    return number
