# time complexity: O(m+n)
# space complexity: O(m+n)
from typing import Optional





class Solution:
    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)

        totalSum = 0
        carry = 0
        result = ListNode()
        while r1 or r2:
            if r1:
                totalSum += r1.val
                r1 = r1.next
            if r2:
                totalSum += r2.val
                r2 = r2.next

            result.val = totalSum % 10
            carry = totalSum // 10
            head = ListNode(carry)
            head.next = result
            result = head
            totalSum = carry

        return result.next if carry == 0 else result
