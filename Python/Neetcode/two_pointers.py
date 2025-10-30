""" Module to encapsulate the problems
 on two pointers

 John Samis - Oct 2025
 """
from Python.Neetcode.base import NeetCodeSection, easy_q, medium_q, hard_q
from typing import override

class TwoPointers(NeetCodeSection):
    """
    Encapsulate the methods and exercises complete in this class

    """
    count_neetcode: int = 5

    @staticmethod
    @easy_q
    def valid_palindrome(s: str) -> bool:
        """return true if s is a palindrome, in which
        it reads forwards: racecar

        restrict: we only want alphanumeric characters, so get rid of
        spaces
        use two pointers to walk inwards """
        left: int = 0
        right: int = len(s) - 1

        while left < right:

            # We also want to skip over spaces and whatnot
            while left < right and not s[right].isalnum():
                right -= 1

            while left < right and not s[left].isalnum():
                left += 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


    @staticmethod
    @easy_q
    def container_with_most_water(heights: list[int]) -> int:
        """ heights[i] represent hte height of the ith bar
        kind of like buckets for the most part, again think in your 3d animation brain
        just like a bucket

        for this we use two pointers as our 'bucket walls' and move
        the smaller one, naturally since our limiting reactant is the smaller one

        we calculate the water as the area sort of

        """
        left: int = 0
        right: int = len(heights) - 1
        most_water: int = 0

        while left < right:
            lowest_height: int = min(heights[left], heights[right])
            curr_water: int = (right - left) * lowest_height
            most_water = max(most_water, curr_water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return most_water

    @staticmethod
    @medium_q
    def two_integer_sum_ii(nums: list[int], target: int) -> list[int]:
        """ sorted ascending order list,
        return the indices of two-nums, such that those numbers add up to
        the target number. I1 nad I2 are never equal whatsoever
        always one solution, and it must be with O(1) space or 'in-place'
        """
        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1

        return []







