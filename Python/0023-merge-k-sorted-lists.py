# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for left in lists:
            while left:
                nodes.append(left.val)
                left = left.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next