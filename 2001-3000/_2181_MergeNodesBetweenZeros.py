# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        solution_cur = ListNode()
        start = solution_cur
        cur = head.next
        value=0

        while cur:
            if cur.val == 0:
                solution_cur.next = ListNode(value)
                solution_cur = solution_cur.next
                value=0
            else:
               value+=cur.val

            cur = cur.next
        return start.next