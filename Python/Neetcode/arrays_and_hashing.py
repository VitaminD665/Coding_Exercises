"""
Part of the Neetcode Roadmap
Array and Hashing problems

John Samis - October 2025
"""
from Python.Neetcode.base import NeetCodeSection, easy_q, medium_q, hard_q
from typing import Optional, List
from collections import defaultdict


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
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        """return a list of nested list that contain a
        collection of anagrams, output in any order,
        same chars as another string, but order is diff

        assumptions: that we only deal with lowercase english letters

        use a dict with an array of ordered letters of the alphabet as the keys
        tuple due to python mutability impossibility as dict keys
        and the values as a list of the grouped anagrams

        """
        anagram_groups = defaultdict(list)
        for s in strs:
            count = [0] * 26  # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1

            anagram_groups[tuple(count)].append(s)

        return list(anagram_groups.values())

    @staticmethod
    @medium_q
    def longest_consecutive_sequence(nums: Optional[list[int]]) -> int:
        """ return the longest consecutive sequence of elements that can be
        formed 
        
        each element is exactly 1 greater than the previous element;
        elements do not have to be consecutive in the original array
        
        if num - 1 DNE in the given array, this can be marked as the 'start' 
        of the series

        Break into steps again, this will likely be useful for future OAs and interviews as well
        1. Convert to hash set first so we get quick lookups
        2. We look for the start of the sequences, this is that if n - 1 DNE in our set
        3. If it is the start, we start looking for n + 1, n + 2, and so on by checking if each is in the
           set and by incrementing a counter
        4. We can place the length of each sequence in a list and then call max
        """
        if nums is None:
            return 0

        s = set(nums)
        max_length: int = 0

        for num in s:
            if num - 1 not in s:
                # This is our sequence starter
                count = 1
                while True:
                    if num + count not in s:
                        break

                    count += 1

                max_length = max(max_length, count)

        return max_length


    @staticmethod
    @medium_q
    def top_k_freq_elements(nums: list[int], k: int) -> list[int]:
        """ return the k most frequent members of the array
        so if k = 2, if 2 is there twice and 3 is there 3 times
        we return [2, 3] because both of them fit the k description

        * order of return does not matter at all.
        so k = 1 for [7, 7] return [7]

        we really want to group numbers based on their frequencies
        from one to n. Then simply pick the top k numbers from the buckets
        from n to 1.

        bucket sort, not super familiar so lets see if I can
        get through what I need to and first principles this bitch

        we want to map the indices/count/freq to values
        where the values are lists of the items that have that

        we will limit our go back from n to 1 via knowing the length of the
        input array. So essentially if n = 6 we can just go back down from 6

        so step wise:
        1. we want to get the freq of each, this can can be done with a hashmap (dict)
        2. Populate our bucket sort
        3. iterate downwards till k times?

        """
        freq: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        count: dict[int, int] = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)

        result: list[int] = list()
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

                if len(result) == k:
                    return result

        return result

    @staticmethod
    @medium_q
    def prod_array_except_self(nums: list[int]) -> list[int]:
        """ return an output array where each element is the product of 
        all of the leements in nums except for nums at that index
        
        don't need to worry about integer size or anything there.

        Solve it in O(n) without using division?
        
        Immediately thinking of hashsets, dicts here.

        We use prefix/suffix here

        """
        if not nums:
            return []

        output: list[int] = [None] * len(nums)

        # So first do left to right
        curr_prod: int = 1
        for i in range(len(nums)):
            output[i] = curr_prod
            curr_prod *= nums[i]

        # Then left to right
        curr_prod = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= curr_prod
            curr_prod *= nums[i]

        return output





