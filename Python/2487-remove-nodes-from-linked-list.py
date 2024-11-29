# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        nextNode = self.removeNodes(head.next)

        if head.val < nextNode.val:
            return nextNode

        head.next = nextNode
        return head


root = ListNode(5)
root.next = ListNode(2)
root.next.next = ListNode(13)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(8)

print(Solution().removeNodes(root))
