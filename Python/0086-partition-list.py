# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessNode, greatNode = ListNode(0), ListNode(0)
        lessHead, greatHead = lessNode, greatNode
        while head != None:
            if head.val < x:
                lessNode.next = head
                lessNode = lessNode.next
            else:
                greatNode.next = head
                greatNode = greatNode.next
            head = head.next

        greatNode.next = None
        lessNode.next = greatHead.next
        return lessHead.next