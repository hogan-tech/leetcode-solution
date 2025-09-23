# time complexity: O(n)
# space complexity: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next

        prev = None
        node = head
        
        for _ in range(k):
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode

        head.next = self.reverseKGroup(node, k)
        return prev

'''
k = 3
  p   n
      |
1 2 3 4 5
    |
'''

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
k = 2
print(Solution().reverseKGroup(root, k))
