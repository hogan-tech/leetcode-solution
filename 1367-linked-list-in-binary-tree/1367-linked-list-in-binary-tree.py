from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        if head is None:
            return True
        if node is None:
            return False
        if head.val != node.val:
            return False
        return self.dfs(head.next, node.left) or self.dfs(head.next, node.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right) or self.dfs(head, root)


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)

root = TreeNode(1)
root.left = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.left = TreeNode(1)
root.right.left.right.right = TreeNode(3)

print(Solution().isSubPath(head, root))
