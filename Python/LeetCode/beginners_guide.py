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


    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        """ return a string array where
        if i is divisible by 3 and 5, add "FIzzBuzz"
        if i is divisible by 3, add "Fizz"
        if i is divisible ny 5, add "Buzz"
        otherwise simply add the number (as a string)

        the key here is the modulo operator which gives you the 'reste'
        """
        output: list[str] = []
        divisors: dict[int, str] = {
            3: "Fizz",
            5: "Buzz",
        }

        for i in range(1, n + 1):
            s: str = ""
            for divisor, label in divisors.items():
                if i % divisor == 0:
                    s += label

            if s:
                output.append(s)
            else:
                output.append(str(i))

        return output






