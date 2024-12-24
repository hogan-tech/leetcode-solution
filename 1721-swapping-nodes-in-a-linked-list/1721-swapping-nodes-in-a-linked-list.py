# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def traverse(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        front, end = None, None
        curr = head
        while curr:
            count += 1
            if end is not None:
                end = end.next

            if count == k:
                front = curr
                end = head
            curr = curr.next

        front.val, end.val = end.val, front.val
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
print(Solution().swapNodes(head, k))
