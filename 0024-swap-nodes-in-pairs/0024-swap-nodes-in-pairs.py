# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        firstNode = head
        secondNode = head.next

        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode
        return secondNode


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
print(Solution().swapPairs(root))
