"""
Module for the linked list questions on neetcode


"""
from scaffolding import MemberCountingMeta
from typing import override, Optional


class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList(metaclass=MemberCountingMeta):
    """
    Encapsulate the linked list questions

    """
    @override
    def __repr__(self):
        pass

    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        """return the new beginning node of a linked list"""
        pass