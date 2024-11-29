# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even = 0
        odd = 0
        gameResult = []
        while head:
            gameResult.append(head.val)
            head = head.next
        for i in range(0, len(gameResult), 2):
            if gameResult[i] > gameResult[i + 1]:
                even += 1
            else:
                odd += 1
        if even == odd:
            return "Tie"
        return "Even" if even > odd else "Odd"


head = ListNode(2)
head.next = ListNode(5)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
print(Solution().gameResult(head))
