# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}
        freqHead = None
        while head:
            if head.val not in freq:
                freq[head.val] = ListNode(1, freqHead)
                freqHead = freq[head.val]
            else:
                freq[head.val].val += 1
            head = head.next
        return freqHead


root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(2)
root.next.next.next = ListNode(1)
root.next.next.next.next = ListNode(2)
root.next.next.next.next.next = ListNode(3)
print(Solution().frequenciesOfElements(root))
