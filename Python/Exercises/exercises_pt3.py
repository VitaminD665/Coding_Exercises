"""
Part 3 to the exercises, certainly getting slightly harder every time
"""
from __future__ import annotations
from typing import override, Optional


def max_subarray(nums: list[int]) -> int:
    curr_sum: int = nums[0]
    max_sum: int = nums[0]

    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum


# Moving onto linked list basics here
class ListNode:
    """ Create a singly linkedlist class, ala your classic C definition."""
    value: int
    next: ListNode | None

    def __init__(self, value: int, next: ListNode | None = None) -> None:
        self.value = value
        self.next = next

    @override
    def __repr__(self):
        return f"ListNode(value={self.value})"

    @override
    def __str__(self):
        return f"ListNode Object, Value: {self.value}, has_next={self.next is not None}"

def reverse_list(head: ListNode | None) -> ListNode | None:
    """reverse the linked list, pass by reference"""

    prev = None
    curr: ListNode = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev

        prev = curr
        curr = next_node

    return prev

def find_middle(head: ListNode | None) -> ListNode | None:
    """ find the middle of a linkedlist, using two pointer slow fast approach"""
    slow: ListNode = head
    fast: ListNode = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def has_cycle(head: ListNode | None) -> bool:
    """ return True if the LL has a looped cycle, otherwise false"""
    slow: ListNode = head
    fast: ListNode = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False

class LinkedList:
    """ Model a singly linked list, composition with ListNode"""
    def __init__(self, head: Optional[ListNode] = None) -> None:
        self.head = head

    def append_node(self, node: ListNode) -> bool:
        """ insert a new node at the end of the list"""
        curr = self.head

        while curr:
            if curr.next is None:
                curr.next = node
                return True

            curr = curr.next

        return False

    @classmethod
    def from_list(cls, initial_list: list[int]) -> LinkedList:
        """ Build a LinkedList from a python list"""
        pass

    @staticmethod
    def to_list(initial_list: LinkedList) -> list[int]:
        """ Convert a LinkedList to a Python list"""
        pass



