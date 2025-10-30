"""
Module for the linked list questions on neetcode

John Samis - Oct 2025
"""
from Python.Neetcode.base import NeetCodeSection, easy_q, medium_q, hard_q
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList(NeetCodeSection):
    """
    Encapsulate the linked list questions

    """
    count_neetcode: int = 11


    @staticmethod
    @easy_q
    def reverse_list(head: ListNode) -> Optional[ListNode]:
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

    @staticmethod
    @easy_q
    def has_cycle(head: ListNode) -> bool:
        """ return true if there is a cycle in the list
        this means that a node can be visited again

        we certainly want to use the slow and fast pointer approach
        """
        if not head:
            return False

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

    @staticmethod
    @easy_q
    def merge_two_lists(list_1: ListNode, list_2: ListNode) -> ListNode:
        """ return the new head of the merge lists from
        given their head nodes; must be sorted
        """
        new_head = result = ListNode()
        while list_1 and list_2:
            if list_1.val < list_2.val:
                result.next = list_1
                list_1 = list_1.next
            else:
                result.next = list_2
                list_2 = list_2.next

            result = result.next

        result.next = list_1 or list_2
        return new_head.next










