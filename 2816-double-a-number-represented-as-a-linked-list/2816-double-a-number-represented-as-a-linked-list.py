# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        val = 0

        while head is not None:
            values.append(head.val)
            head = head.next

        newTail = None

        while values or val != 0:
            newTail = ListNode(0, newTail)

            if values:
                val += values.pop() * 2
            newTail.val = val % 10
            val //= 10

        return newTail


root = ListNode(1)
root.next = ListNode(8)
root.next.next = ListNode(9)
print(Solution().doubleIt(root))
