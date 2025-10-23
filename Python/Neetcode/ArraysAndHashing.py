"""
Part of the Neetcode Roadmap
Array and Hashing problems

John Samis - October 2025
"""
from Python.Neetcode.base import NeetCodeSection, easy_q, medium_q, hard_q


class ArraysAndHashing(NeetCodeSection):
    """
    Contains the Arrays and Hashing Exercises as part of the NeetCode DSA Roadmap
    """
    count_neetcode: int = 9

    @staticmethod
    @easy_q
    def contains_duplicate(nums: list[int]) -> bool:
        """
        Return true if any value in the input array nums appears more than once
        """
        return len(set(nums)) != len(nums)

    @staticmethod
    @easy_q
    def two_sum(nums: list[int], target: int) -> list[int]:
        """ Array of ints nums, int target,
        return the indices i and j so that they do the thing"""
        store: dict[int, int] = {}

        for i in range(len(nums)):
            if target - nums[i] in store:
                return [store[target- i], i]

            store[nums[i]] = i

        return []

    @staticmethod
    @easy_q
    def valid_anagram(s: str, t: str) -> bool:
        """ Return true if tthe two input strings s, t are
        anagrams contains the same characters as another string,
        but the order differs

        assumption: s, t are lowercase english letters

        since we don't care about order, they are guaranteed to have the
        amount of characters, thus using sorting should work

        do a frequency count, then compare the dicts
        """
        s_frq: dict = {}
        for c in s:
            if c in s_frq:
                s_frq[c] += 1
            else:
                s_frq[c] = 1

        t_frq: dict = {}
        for c in t:
            if c in t_frq:
                t_frq[c] += 1
            else:
                t_frq[c] = 1

        return t_frq == s_frq

    @staticmethod
    @medium_q
    def group_anagrams(strs: list[str]) -> list[list[str]]:
        """return a list of nested list that contain a
        collection of anagrams, output in any order,
        same chars as another string, but order is diff

        assumptions: that we only deal with lowercase english letters
        Let's break it up.

        We certainly want to loop over every
        element in strs.


        """
        pass












