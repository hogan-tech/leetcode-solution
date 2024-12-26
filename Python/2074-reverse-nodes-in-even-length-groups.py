# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        groupLength = 2
        while prev.next:
            node = prev
            n = 0
            for _ in range(groupLength):
                if node.next is None:
                    break
                node = node.next
                n += 1
            if n % 2:
                prev = node
            else:
                reverse = node.next
                curr = prev.next
                for _ in range(n):
                    currNext = curr.next
                    curr.next = reverse
                    reverse = curr
                    curr = currNext
                prevNext = prev.next
                prev.next = node
                prev = prevNext
            groupLength += 1
        return head


head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(9)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next.next = ListNode(4)
print(Solution().reverseEvenLengthGroups(head))
