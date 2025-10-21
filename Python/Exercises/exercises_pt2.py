"""
This module is to contain the exercises done 'for fun/warmup' to the harder programming
questions I might be asked later on.

John Samis - Sept 2025
"""

def count_frequencies(nums: list[int]) -> dict[int, int]:
    """ return a dict that maps each number to the number of time it appears"""
    res: dict = {}

    for num in nums:
        if num not in res:
            res[num] = 0

        res[num] += 1

    return res

def avg_word_length(text: str) -> float:
    """ return the avg length of the words in the string, assume nice input"""
    if text == "":
        return 0.0

    words: list = text.split()
    n_words: int = len(words)

    return sum([len(word) for word in words]) / n_words

def find_min(nums: list[int]) -> int | None:
    """ smallest int"""
    if not nums:
        return None

    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    return smallest

def reverse_list(nums: list[int]) -> list[int]:
    """ title"""
    res = []

    if not nums:
        return res

    for i in nums:
        res.insert(0, i)

    return res

def reverse_in_place(nums: list[int]) -> None:
    """ reverse but with O(1) space"""
    #Use two pointers

    left = 0
    right = len(nums) - 1

    # Similar to binary search
    while left < right:
        # we want to swap their values essentially
        nums[left], nums[right] = nums[right], nums[left]

        #then we bring them both closer and the while condition will handle it for us
        left += 1
        right -= 1

def is_palindrome(seq: str | list) -> bool:
    """ true if it is"""
    if not seq:
        return True

    left: int  = 0
    right: int = len(seq) - 1

    while left < right:

        if seq[left] != seq[right]:
            return False

        left += 1
        right -= 1

    return True

def remove_element(nums: list[int], val: int) -> int:
    """ remove all instances of val from nums and return length"""

    return len([num for num in nums if num != val])

def remove_in_place(nums: list[int], val: int) -> int:
    """ same thing, but with no extra space"""
    k: int = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

def remove_duplicates_in_place(nums: list[int]) -> int:
    """ return the length of the new list while also modifying the original list"""
    # assume list is sorted
    # Idea is the slow fast, we want to use pointers here most certainly
    if not nums:
        return  0

    s_ptr: int = 0

    for f_ptr in range(len(nums)):
        if nums[f_ptr] != nums[s_ptr]:
            nums[s_ptr] = nums[f_ptr]
            s_ptr += 1

    return s_ptr + 1 # we add one for index?

def two_sum(nums: list [int], target: int) -> list[int]:
    """ return the indices of two numbers that add up to target"""
    # If one tries to brute force every pair they will die
    seen: dict[int, int] = {}

    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [seen[target - i], i]

        seen[nums[i]] = i # we have the k as the number and the v as the index

    return []

def contains_duplicate(nums: list[int]) -> bool:
    """ return true if any number appears at least twice in the list and false if every
    element is unique"""
    return len(nums) != len(set(nums))


def majority_element(nums: list[int]) -> int | None:
    """ return the element that appears more than n/2 times in the list
    where n is the length of the list"""
    if not nums:
        return None

    freq: dict[int, int] = {}

    for num in nums:

        if num in freq:
            freq[num] += 1
        elif num not in freq:
            freq[num] = 1

        if freq[num] > len(nums) // 2:
            return num

    return None

def max_profit(prices: list[int]) -> int:
    """ return the max profit one can achieve by buying one day and selling
    on another, if no profit is possible return 0, assume all positive ints"""
    if not prices:
        return 0

    min_p: int = prices[0]
    max_prof: int = 0

    for price in prices:
        if price < min_p:
            min_p = price

        profit: int = price - min_p
        if profit > max_prof:
            max_prof = profit

    return max_prof if max_prof > 0 else 0

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """ return a list of the unique elements present in both arrays"""
    set1, set2  = set(nums1), set(nums2)


    # This is actually really cool! Python's bitwise operators don't have the
    # same behaviour for numbers and for sets. On sets its actually the
    # namesake set theory computations. Very cool
    return list(set1 & set2)