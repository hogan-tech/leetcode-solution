# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeSeen = set()
        node = head
        while node is not None:
            if node in nodeSeen:
                return node
            else:
                nodeSeen.add(node)
                node = node.next
        return None


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

print(Solution().detectCycle(head))
