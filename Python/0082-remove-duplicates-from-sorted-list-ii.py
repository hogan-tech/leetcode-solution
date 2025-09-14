# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr, prev = head, dummy
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return dummy.next


def traverse(node: Optional[ListNode]):
    if node is None:
        return
    print(node.val)
    traverse(node.next)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
traverse(Solution().deleteDuplicates(head))
