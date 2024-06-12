# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        oldTail = head
        n = 1
        while oldTail.next:
            oldTail = oldTail.next
            n += 1

        k = k % n
        oldTail.next = head
        newTail = head
        for i in range(1, n-k):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None
        return newHead


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
k = 2
print(Solution().rotateRight(root, k))
