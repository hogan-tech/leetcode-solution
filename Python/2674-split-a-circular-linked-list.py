# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        slow, fast = list, list.next
        while fast.next != list:
            slow = slow.next
            if fast.next.next != list:
                fast = fast.next.next
            else:
                fast = fast.next
        nextList = slow.next
        slow.next = list
        fast.next = nextList
        return [list, nextList]


head = ListNode(1)
head.next = ListNode(5)
head.next.next = ListNode(7)
head.next.next.next = head
print(Solution().splitCircularLinkedList(head))
