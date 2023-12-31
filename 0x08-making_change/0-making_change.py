#!/usr/bin/python3
"""
Module for making change
"""

from collections import defaultdict


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    dp = defaultdict(lambda: float('inf'))
    dp[0] = 0

    # Iterate through all coin values
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
