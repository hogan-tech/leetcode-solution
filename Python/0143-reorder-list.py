# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first = head
        second = prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        return


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
print(Solution().reorderList(root))
