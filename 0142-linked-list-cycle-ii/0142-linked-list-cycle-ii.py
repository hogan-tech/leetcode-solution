# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeSeen = set()
        node = head
        while node:
            if node in nodeSeen:
                return node
            nodeSeen.add(node)
            node = node.next
        return None

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        fast = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(Solution().detectCycle(head))
