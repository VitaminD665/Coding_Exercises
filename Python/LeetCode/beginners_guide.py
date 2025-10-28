"""
A module to contain the exercises and notes on the Leetcode beginner's guide section

John Samis - October 2025
"""
from typing import List


class BeginnersGuide:

    @staticmethod
    def add_two_integers(num1: int, num2: int) -> int:
        return num1 + num2

    @staticmethod
    def running_sum_1d_array(nums: List[int]) -> List[int]:
        """ return the running sum of the array"""
        output: list[int] = []
        prev_sum: int = 0

        for num in nums:
            prev_sum += num
            output.append(prev_sum)

        return output

    @staticmethod
    def richest_customer_wealth(accounts: List[List[int]]) -> int:
        """ given mxn integer grid accounts, accounts[i][j] is
        amount of money for the ith customer at the jth bank

        return the wealth that the richest customer has; wealth
        is the sum of all of a customers accounts"""

        max_wealth: int = 0
        for customer in accounts:
            customer_sum: int = 0
            for balance in customer:
                customer_sum += balance

            max_wealth = max(max_wealth, customer_sum)

        return max_wealth













