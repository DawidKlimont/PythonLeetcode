# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        node.val = l1.val+l2.val
        leftover = 0
        if node.val >= 10:
            node.val -= 10
            leftover += 1
        if l1.next!=None and l2.next!=None:
            l1.next.val+=leftover
            node.next = self.addTwoNumbers(l1.next, l2.next)
        elif l1.next==None and l2.next!=None:
            l2.next.val+=leftover
            node.next = self.addTwoNumbers(ListNode(), l2.next)
        elif l1.next!=None and l2.next==None:
            l1.next.val+=leftover
            node.next = self.addTwoNumbers(l1.next, ListNode())
        elif leftover>0:
            node.next = ListNode(leftover)


        return node