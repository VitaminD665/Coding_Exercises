"""
Part of the Neetcode Roadmap
Array and Hashing problems

John Samis - October 2025
"""
from scaffolding import MemberCountingMeta
from typing import override

class ArraysAndHashing(metaclass=MemberCountingMeta):
    """
    Contains the Arrays and Hashing Exercises as part of the NeetCode DSA Roadmap
    """
    count_neetcode: int = 9

    @override
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"num_questions_solved={self.num_questions}, "
                f"out_of={self.count_neetcode}, "
                f"list={self.list_questions})")

    @staticmethod
    def contains_duplicate(nums: list[int]) -> bool:
        """
        Return true if any value in the input array nums appears more than once
        """
        return len(set(nums)) != len(nums)

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        """ Given an array of integers nums, and an integer target,
        return the indices i and j so that they do the thing"""
        store: dict[int, int] = {}

        for i in range(len(nums)):
            if target - nums[i] in store:
                return [store[target- i], i]

            store[nums[i]] = i

        return []

