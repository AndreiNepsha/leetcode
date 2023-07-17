from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        n1s, n2s = 0, 0
        while n1 or n2:
            if n1:
                n1s += 1
                n1 = n1.next
            if n2:
                n2s += 1
                n2 = n2.next

        max_size = max(n1s, n2s)
        n1start = max_size - n1s
        n2start = max_size - n2s
        head = ListNode(0)
        
        def calculate(n: ListNode, i: int, n1: ListNode, n2: ListNode):
            if i == max_size:
                return
            if i >= n1start and i >= n2start:
                n.next = ListNode(n1.val + n2.val)
                calculate(n.next, i + 1, n1.next, n2.next)
            elif i >= n1start:
                n.next = ListNode(n1.val)
                calculate(n.next, i + 1, n1.next, n2)
            else:
                n.next = ListNode(n2.val)
                calculate(n.next, i + 1, n1, n2.next)
            if n.next.val >= 10:
                n.next.val = n.next.val % 10
                n.val += 1
        calculate(head, 0, l1, l2)

        return head if head.val else head.next
