# time complexity: O(n+m)
# space complexity: O(m)
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> ListNode:
        nodesBSet = set()

        while headB:
            nodesBSet.add(headB)
            headB = headB.next

        while headA:
            if headA in nodesBSet:
                return headA
            headA = headA.next

        return None


headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)


headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = ListNode(8)
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)

print(Solution().getIntersectionNode(headA, headB))
