# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        tail, con = cur, prev

        while right:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur

        return head
