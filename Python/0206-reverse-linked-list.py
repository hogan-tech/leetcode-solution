# time complexity: O(n)
# space complexity: O(1)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev



# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if (not head) or (not head.next):
#             return head

#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)

print(Solution().reverseList(root))
