from heapq import heappop, heappush
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # not efficient
    def _mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        curs = [l for l in lists if l is not None]
        l = len(curs)
        
        head = None
        last = None
        done = 0

        while done < l:
            mi = 0
            while not curs[mi]:
                mi += 1
            for i in range(mi + 1, l):
                if curs[i] and curs[i].val < curs[mi].val:
                    mi = i

            if not head:
                head = ListNode(curs[mi].val)
                last = head
            else:
                last.next = ListNode(curs[mi].val)
                last = last.next

            if not curs[mi].next:
                done += 1
            curs[mi] = curs[mi].next
        
        return head

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        head = ListNode() # "fake" pre-head element
        c = head

        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i))
        
        while heap:
            val, i = heappop(heap)

            c.next = ListNode(val)
            c = c.next

            lists[i] = lists[i].next
            if lists[i]:
                heappush(heap, (lists[i].val, i))

        return head.next