# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None

        def dfs(currNode: TreeNode, p: TreeNode, q: TreeNode):
            if currNode is None:
                return False
            left, right, mid = False, False, False
            if p == currNode or q == currNode:
                mid = True
            left = dfs(currNode.left, p, q)
            if not self.lca:
                right = dfs(currNode.right, p, q)

            if mid + left + right >= 2:
                self.lca = currNode
                
            return mid or left or right

        dfs(root, p, q)
        return self.lca


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

solution = Solution()
result = solution.lowestCommonAncestor(root, root.left, root.right)
