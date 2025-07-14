# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binaryInt = ""
        while head:
            binaryInt += str(head.val)
            head = head.next
        return int(binaryInt, 2)


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
print(Solution().getDecimalValue(head))
