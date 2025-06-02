# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        result = []
        curr = head
        currIdx = -1
        while curr:
            currIdx += 1
            result.append(0)
            while stack and stack[-1][1] < curr.val:
                lastIdx, _ = stack.pop()
                result[lastIdx] = curr.val
            stack.append([currIdx, curr.val])
            curr = curr.next

        return result


'''
[5,5,0]
[7,0,5,5,0]
'''
head1 = ListNode(2)
head1.next = ListNode(1)
head1.next.next = ListNode(5)
print(Solution().nextLargerNodes(head1))
head2 = ListNode(2)
head2.next = ListNode(7)
head2.next.next = ListNode(4)
head2.next.next.next = ListNode(3)
head2.next.next.next.next = ListNode(5)
print(Solution().nextLargerNodes(head2))
