# Definition for singly-linked list.
from math import gcd
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def insertGreatestCommonDivisors( head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current.next:
        next_current = current.next
        minDiv = gcd(current.val,next_current.val)

        current.next = ListNode(minDiv, next_current)
        current = next_current
    return head

def test(val):
    head = ListNode(val[0])
    prev = head
    for i in range(1,len(val)):
        cur = ListNode(val[i])
        prev.next = cur
        prev = cur

    cur = insertGreatestCommonDivisors(head)
    result=[]
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

print(test([18,6,10,3,69,12,451,515523,1215]))