"""
Module for the linked list questions on neetcode

John Samis - Oct 2025
"""
from Python.Neetcode.scaffolding import NeetCodeSection
from typing import override, Optional


class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList(NeetCodeSection):
    """
    Encapsulate the linked list questions

    """
    @staticmethod
    def reverse_list(head: ListNode) -> Optional[ListNode] :
        """return the new beginning node of a linked list
        we need to 'walk' the list and simply switch the orientation
        of the pointers at any given node

        head -> next -> next -> next -> next -> null
        """
        if head is None:
            return None

        current = head
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous


print(LinkedList())