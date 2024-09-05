#!/usr/bin/python3
"""
Prime game winner determination
"""


def isWinner(x, nums):
    """
    Determining the winner of a prime game
    """
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for x in range(2, int(n**0.5) + 1):
        if primes[x]:
            for y in range(x**2, n + 1, x):
                primes[y] = False

    for n in nums:
        count = sum(primes[2:n+1])
        ben_wins += count % 2 == 0
        maria_wins += count % 2 == 1

    if maria_wins == ben_wins:
        return None

    return 'Maria' if maria_wins > ben_wins else 'Ben'
