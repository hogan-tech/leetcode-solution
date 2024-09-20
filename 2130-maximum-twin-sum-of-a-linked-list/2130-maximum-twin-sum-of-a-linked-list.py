from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        maxSum = 0
        while head:
            arr.append(head.val)
            head = head.next
        for i in range(len(arr) // 2):
            maxSum = max(maxSum, arr[i] + arr[len(arr) - 1 - i])
        return maxSum


head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(Solution().pairSum(head))
