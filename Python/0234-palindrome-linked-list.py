# time complexity: O(n)
# space complexity: O(n)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindromList = []
        while head:
            palindromList.append(head.val)
            head = head.next
        i = 0
        j = len(palindromList) - 1
        while i < j:
            if palindromList[i] != palindromList[j]:
                return False
            i += 1
            j -= 1

        return True


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(2)
root.next.next.next = ListNode(1)
print(Solution().isPalindrome(root))
