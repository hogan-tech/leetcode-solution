# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List, Optional



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for left in lists:
            while left:
                nodes.append(left.val)
                left = left.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)
node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)
node3 = ListNode(2)
node3.next = ListNode(6)
print(Solution().mergeKLists([node1, node2, node3]))
print(Solution().mergeKLists([]))
print(Solution().mergeKLists([[]]))
