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
    def valid_parentheses():
        pass

    @staticmethod
    @medium_q
    @has_inner_class
    def min_stack():
        """ We must define a class inside of this method"""
        class MinStack:
            """
            Stack class that supports push, pop, top, getMin ops.
            Valid for ints only
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
                pass

            def get_min(self) -> int:
                pass