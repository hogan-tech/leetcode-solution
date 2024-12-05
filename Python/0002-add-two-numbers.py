# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        resultTail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)

            resultTail.next = ListNode(out)
            resultTail = resultTail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


l1 = ListNode(0)

l2 = ListNode(0)

print(Solution().addTwoNumbers(l1, l2))
