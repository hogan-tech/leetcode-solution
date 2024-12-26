# time complexity: O(n)
# space complexity: O(1)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None] * k
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        width, remainder = divmod(count, k)

        curr = head
        prev = curr
        for i in range(k):
            new = curr
            currSize = width
            if remainder > 0:
                remainder -= 1
                currSize += 1
            for _ in range(currSize):
                prev = curr
                if curr:
                    curr = curr.next
            if prev is not None:
                prev.next = None
            result[i] = new
        return result


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
k = 5
print(Solution().splitListToParts(node, k))
