"""
Module for the Stack section of questions

John Samis - Oct 2025
"""
from Python.Neetcode.base import (NeetCodeSection,
                                  easy_q, medium_q, hard_q, has_inner_class)



class Stack(NeetCodeSection):
    """
    Stack section on neetcode and whatnot, cook up yk


    """
    count_neetcode: int = 7

    @staticmethod
    @easy_q
    def valid_parentheses(s: str) -> bool:
        """ The classic problem which involves using a hashtable for the most
        optimal solution indeed. We will use a stack to store characters 
        iterate through index and. opening bracket, we push onto the stack, 
        if closing type, we check the top of the stack which is indeed O(1) peek or peep
        
        If it is not corresponding, its gone immediately and we return false
        """
        if len(s) % 2 != 0:
            return False

        stack: list[str] = []
        pairs: dict[str, str] = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        openings: set[str] = set(pairs.values())

        for c in s:
            if c in openings:
                stack.append(c)
            elif c in pairs:
                if not stack:
                    return False
                
                if stack.pop() != pairs[c]:
                    return False
            else:
                return False

        return not stack

    @staticmethod
    @medium_q
    @has_inner_class
    def min_stack():
        """ We must define a class inside of this method"""
        class MinStack:
            """
            Stack class that supports push, pop, top, getMin ops.
            Valid for ints only, each class member method should be O(1)
            """
            def __init__(self) -> None:
                """ dunda"""
                pass

            def push(self, value: int) -> None:
                """ pushes element value onto the stack"""
                pass

            def pop(self) -> None:
                """ remove the element on the top of the list"""
                pass

            def top(self) -> int:
                """ get and return the top element in the list"""
                pass

            def get_min(self) -> int:
                """ get the minimum element in the stack"""
                pass