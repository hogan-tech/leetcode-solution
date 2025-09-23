# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return

        node = head
        prev = None
        for _ in range(left - 1):
            prev = node
            node = node.next
            right -= 1

        tail, con = node, prev
        for _ in range(right):
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = node
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
left = 2
right = 4
traverse(Solution().reverseBetween(head, left, right))
