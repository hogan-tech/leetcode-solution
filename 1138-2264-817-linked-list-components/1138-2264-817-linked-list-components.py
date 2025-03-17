# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numsSet = set(nums)
        node = head
        inNumSet = False
        result = 0
        while node:
            if node.val in numsSet:
                if not inNumSet:
                    inNumSet = True
                    result += 1
            else:
                inNumSet = False
            node = node.next
        return result


head1 = ListNode(0)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(3)
nums = [0, 1, 3]
print(Solution().numComponents(head1, nums))
head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(3)
head2.next.next.next.next = ListNode(4)
print(Solution().numComponents(head2, nums))
