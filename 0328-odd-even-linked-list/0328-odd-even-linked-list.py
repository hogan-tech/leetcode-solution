# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd, even = ListNode(0), ListNode(0)
        evenHead = even
        oddHead = odd
        idx = 1
        while head:
            if idx % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            idx += 1
            head = head.next
        even.next = None
        odd.next = evenHead.next
        return oddHead.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
print(Solution().oddEvenList(root))
