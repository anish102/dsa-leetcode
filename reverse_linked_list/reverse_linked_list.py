"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# We initialize two pointers: `prev` and `cur`. `prev` starts as None because the first node
# will eventually point to None, and `cur` starts as the head of the list.
# If the list is empty or contains only one element, return the head as is.
# In the loop, we reverse the next pointer of the current node (cur) to point
# to the previous node (prev), then move both pointers one step forward until all
# nodes are reversed. Finally, we return prev,
# which points to the new head of the reversed list.
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head
    if not head or not head.next:
        return head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev
