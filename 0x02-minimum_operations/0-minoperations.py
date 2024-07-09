#!/usr/bin/env python3
'''
method that calculates the fewest number of
operations needed to result in exactly n H characters
'''


def minOperations(n):
    '''
    method that calculates the fewest number of
    operations needed to result in exactly n H characters
    '''
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
