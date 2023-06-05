from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        ah = None
        an = None
        m = 0
        while n1 is not None or n2 is not None:
            s = 0
            if n1 is not None:
                s += n1.val
            if n2 is not None:
                s += n2.val

            if an is None:
                ah = ListNode(s % 10)
                an = ah
            else:
                an.next = ListNode((s + m) % 10 )
                an = an.next
            m = (s + m) // 10

            if n1 is not None:
                n1 = n1.next
            if n2 is not None:
                n2 = n2.next
        if m > 0:
            an.next = ListNode(m)
        return ah
