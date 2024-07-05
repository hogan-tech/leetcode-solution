from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticalNodeIdx = []
        currIdx = 0
        while head and head.next and head.next.next:
            if head.val < head.next.val and head.next.next.val < head.next.val:
                criticalNodeIdx.append(currIdx+2)
            if head.val > head.next.val and head.next.next.val > head.next.val:
                criticalNodeIdx.append(currIdx+2)
            head = head.next
            currIdx += 1
        if len(criticalNodeIdx) < 2:
            return [-1, -1]
        maxDistance = criticalNodeIdx[-1] - criticalNodeIdx[0]
        minDistance = float("inf")
        for i in range(0, len(criticalNodeIdx)-1):
            minDistance = min(
                minDistance, abs(criticalNodeIdx[i] - criticalNodeIdx[i + 1]))
        return [minDistance, maxDistance]


head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(2)

print(Solution().nodesBetweenCriticalPoints(head))
