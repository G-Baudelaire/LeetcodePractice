from sys import prefix
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        node = dummy

        for i in range(left - 1):
            node = node.next
        prefix = node
        reversed_head = node.next

        for _ in range(right - left + 1):
            node = node.next
        suffix = node.next
        node.next = None

        reversed_head, reversed_tail = self.reverseLinkedList(reversed_head)
        prefix.next = reversed_head
        reversed_tail.next = suffix

        return dummy.next

    def reverseLinkedList(self, head: Optional[ListNode]):
        previous_node = None
        node = head

        while node is not None:
            temp = node.next
            node.next = previous_node
            previous_node = node
            node = temp

        return previous_node, head