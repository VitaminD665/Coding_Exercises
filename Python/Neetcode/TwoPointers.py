""" Module to encapsulate the problems
 on two pointers

 John Samis - Oct 2025
 """
from Python.Neetcode.scaffolding import NeetCodeSection
from typing import override

class TwoPointers(NeetCodeSection):
    """
    Encapsulate the methods and exercises complete in this class

    """
    count_neetcode: int = 5

    @staticmethod
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

