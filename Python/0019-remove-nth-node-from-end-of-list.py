# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        countNode = resNode = head
        while countNode:
            total += 1
            countNode = countNode.next
        delIdx = total - n - 1
        if delIdx < 0:
            head = head.next
            return head
        currentIdx = 0
        while resNode:
            if currentIdx == delIdx:
                if resNode.next.next:
                    resNode.next = resNode.next.next
                else:
                    resNode.next = None
                return head
            else:
                resNode = resNode.next
            currentIdx += 1
        return head


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
print(Solution().removeNthFromEnd(root, 2))
