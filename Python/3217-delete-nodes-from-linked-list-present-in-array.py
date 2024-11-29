# time complexity: O(m+n)
# space complexity: O(m)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsSet = set(nums)
        temp = ListNode(next=head)
        curr = temp
        while curr.next:
            if curr.next.val in numsSet:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return temp.next


nums = [1, 2, 3]
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
print(Solution().modifiedList(nums, root))
