# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reader = head.next
        writer = head
        while reader:
            if reader.val:
                writer.val += reader.val
            elif reader.next:
                writer = writer.next
                writer.val = 0
            else:
                writer.next = None
            reader = reader.next
        return head


root = ListNode(0)
root.next = ListNode(3)
root.next.next = ListNode(1)
root.next.next.next = ListNode(0)
root.next.next.next.next = ListNode(4)
root.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next = ListNode(2)
root.next.next.next.next.next.next.next = ListNode(0)
print(Solution().mergeNodes(root))
