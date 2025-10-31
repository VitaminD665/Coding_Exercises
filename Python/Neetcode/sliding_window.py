"""
Module for the sliding window technique

John Samis - October 2025
"""
from Python.Neetcode.base import NeetCodeSection, easy_q, medium_q, hard_q
from collections import defaultdict


class SlidingWindow(NeetCodeSection):
    """ Slide to the left! Sliiiideeeee to the right!"""

    count_neetcode: int = 6

    @staticmethod
    @easy_q
    def best_time__stock(prices: list[int]) -> int:
        """ return the max profit one can achieve
            given the two prices and whatnot

            we use the title track, two pointers to solve this!
        """
        if len(prices) < 2:
            return 0

        max_profit: int = 0
        left: int = 0
        right: int = 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
            right += 1

        return max_profit


