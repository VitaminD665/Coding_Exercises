"""
Binary Search Neetcode section

John Samis - Oct 2025
"""
from Python.Neetcode.base import (NeetCodeSection,
                                  easy_q, medium_q, hard_q, has_inner_class)


class BinarySearch(NeetCodeSection):
    """
    Section for problems related to performing binary searches

    """
    @staticmethod
    @easy_q
    def binary_search(nums: list, target) -> int:
        """ distinct intergers nums, is sorted in ascending order
            and the target,

            look for target in nums, if it exists return its INDEX not value
            otherwise, return -1

            this is the classic binary_search algorithm

            notes afterwards, it is very important to really get
            the basic tech, acquiring middle, the comparison to the value vs. indexes
            and reading a question carefully and returning the index
        """
        left, right = 0, len(nums) - 1

        while left <= right:

            # we want the middle at every iteration
            middle = (left + right) // 2

            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            elif target == nums[middle]:
                return middle

        return -1





