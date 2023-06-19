from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        l = 1
        last = head
        while last.next:
            l += 1
            last = last.next
        
        k = k % l
        if not k:
            return head

        last.next = head

        k = l - k
        i = 0
        prev = None
        n = head
        while i < k:
            prev = n
            n = n.next
            i += 1
        prev.next = None
        return n
