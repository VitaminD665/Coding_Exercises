"""
Binary Search Neetcode section

John Samis - Oct 2025
"""
from typing import Any

from Python.Neetcode.base import (NeetCodeSection,
                                  easy_q, medium_q, hard_q, has_inner_class)


class BinarySearch(NeetCodeSection):
    """
    Section for problems related to performing binary searches

    """
    @staticmethod
    @easy_q
    def binary_search(nums: list, target) -> int:
        """ distinct integers nums, is sorted in ascending order
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

    @staticmethod
    @medium_q
    def search_a_2d_matrix(matrix: list[list[int]], target: int) -> bool:
        """ return true if target exists within the 2d matrix 'matrix'

        each row is in ascending order... the start of each row is greater
        than the last integer of the previous row...

        *key is that this 2d matrix is effectively, 'sorted in ascending order'
        that is where the binary search algorithm shines undoubtedly

        initial soln, just double for loop it

        cannot simply hashset it, list container is unhashable, give typeerror

        is the optimal solution to simply execute multiple binary searches?
        this would coincide with the desired  O(log(m*n))
        """
        if not matrix or not matrix[0]:
            return False

        def inner_bs(row: list[int]) -> bool:
            _left, _right = 0, len(row) - 1

            while _left <= _right:

                _middle = (_left + _right) // 2

                if target > row[_middle]:
                    _left = _middle + 1
                elif target < row[_middle]:
                    _right = _middle - 1
                elif target == row[_middle]:
                    return True

            return False

        left, right = 0, len(matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            first = matrix[middle][0]
            last = matrix[middle][-1]

            if target < first:
               right = middle - 1
            elif target > last:
                left = middle + 1
            elif target == first or target == last:
                return True
            elif first < target < last:
                return inner_bs(matrix[middle])

        return False



























