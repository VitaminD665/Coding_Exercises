"""
File for the python exercise I am doing on the station pc!

John Samis - Sept 2025
"""
def is_even(n: list) -> list:
  
    res: list[bool] = []
    for i in n:
        if i % 2 == 0:
            res.append(True)
        else: 
            res.append(False)
    # or just do a comprehension somehow
    # return []

    return res

def reverse_string(s: str) -> str:
    """ reverse a string """
    # note for splicing [start:end:step]  
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """ Check if a string is the same forwards as backwards"""
    return s == reverse_string(s)

def find_max(nums: list[int]) -> int:
    """ return the largest element in a (assumed) unsorted list """
    ma: int = nums[0]
    for num in nums:
        if nums[num] > ma:
            ma = num

    return ma

def manual_sum(nums: list[int]) -> int:
    """ return the sum of all numbers in the list without sum()"""
    count: int = 0
    for i in nums:
        count += 1

    return count

def contains(nums: list[int], target: int) -> bool:
    """ is target in nums """
    return any(i == target for i in nums)

def count_evens(nums: list[int]) -> int:
    """ return how many times an even number appears """
    count: int = 0 
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

class BankAccount:
    """
    Class for an exercise on oop
    """
    balance: float
    
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        # self.balance -= amount if self.balance >= amount else raise RuntimeError("Not enough balance")

        if self.balance >= amount:
            self.balance -= amount 
        else:
            raise RuntimeError("Not enough balance")

    def get_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"Balance: {self.balance}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(balance={self.balance})"


def count_vowels(s: str) -> int:
    """ return how many vowels are i nthe string"""
    count: int = 0

    for c in s:
        if c.lower() in "aeiou":
            count += 1

    return count

def merge_lists(a: list[int], b: list[int]) -> list[int]:
    """merge these two lists"""
    for i in b:
        a.append(i)
    
    return a 

def remove_duplicate(nums: list[int]) -> list[int]:
    """remove any duplicate elements from a list"""
    # return list(set(nums))
    if not nums:
        return []

    res = [nums[0]]
    for num in nums[1:]:
        if num != res[-1]:
            res.append(num)

    # honestly this one truly preserves the idea of asking, clarifying nad the edge case handling
    return res


def move_zeroes(nums: list[int]) -> list[int]:
    """move all the zeroes to the end of the list while keeping the order of others"""

    zeroes: list = [nums.pop(num) for num in nums if num == 0]
    
    return nums + zeroes # fix this, is wrong


def square_list(nums: list[int]) -> list[int]:
    """square it"""
    return [i**2 for i in nums]

def running_sum(nums: list[int]) -> list[int]:
    """ return a list in which each elemetn is the sum of all numbers up to that index"""

    r_sum: int = 0
    r_sum_list: list[int] = []

    for i in range(len(nums)):
        r_sum += nums[i]
        r_sum_list.append(r_sum)
    
    return r_sum_list