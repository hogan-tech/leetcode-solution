


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeSeen = set()
        node = head
        while node:
            if node in nodeSeen:
                return node
            nodeSeen.add(node)
            node = node.next
        return None


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(Solution().detectCycle(head))
