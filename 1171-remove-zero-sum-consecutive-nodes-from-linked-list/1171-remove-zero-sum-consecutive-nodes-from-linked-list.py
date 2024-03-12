# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefixSum = 0
        prefixSums = {0: dummy}
        current = head

        while current:
            prefixSum += current.val
            if prefixSum in prefixSums:
                toDel = prefixSums[prefixSum].next
                tempSum = prefixSum + toDel.val
                while toDel != current:
                    del prefixSums[tempSum]
                    toDel = toDel.next
                    tempSum += toDel.val
                prefixSums[prefixSum].next = current.next
            else:
                prefixSums[prefixSum] = current
            current = current.next

        return dummy.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(-1)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(1)

print(Solution().removeZeroSumSublists(root))
