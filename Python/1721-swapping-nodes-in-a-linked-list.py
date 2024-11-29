# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def traverse(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        originalList = []
        temp = head
        while temp:
            originalList.append(temp.val)
            temp = temp.next

        originalList[k - 1], originalList[len(originalList) - k] = originalList[len(
            originalList) - k], originalList[k - 1]

        result = newHead = ListNode(originalList[0])
        for i in range(1, len(originalList)):
            tempHead = ListNode(originalList[i])
            newHead.next = tempHead
            newHead = newHead.next

        return result


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
print(Solution().swapNodes(head, k))
