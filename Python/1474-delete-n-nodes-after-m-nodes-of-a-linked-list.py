# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = head
        last = head
        while curr:
            for _ in range(m):
                if curr:
                    last = curr
                    curr = curr.next

            for _ in range(n):
                if curr:
                    curr = curr.next

            last.next = curr
        return head


def traverse(node: Optional[ListNode]):
    if node is None:
        return
    print(node.val)
    traverse(node.next)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)
head.next.next.next.next.next.next.next.next.next.next = ListNode(11)
head.next.next.next.next.next.next.next.next.next.next.next = ListNode(12)
head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(13)
m = 2
n = 3
traverse(Solution().deleteNodes(head, m, n))
