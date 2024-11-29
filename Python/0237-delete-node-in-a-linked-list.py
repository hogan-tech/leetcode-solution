# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next



