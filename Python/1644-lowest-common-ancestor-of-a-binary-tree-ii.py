class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def LCA(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not node:
            return node
        if node == p or node == q:
            return node
        left = self.LCA(node.left, p, q)
        right = self.LCA(node.right, p, q)

        if left and right:
            return node
        elif left:
            return left
        else:
            return right
        

    def DFS(self, node: 'TreeNode', target: int) -> bool:
        if node == target:
            return True
        if node is None:
            return False
        return self.DFS(node.left, target) or self.DFS(node.right, target)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        result = self.LCA(root, p, q)
        if result == p:
            return p if self.DFS(p, q) else None
        elif result == q:
            return q if self.DFS(q, p) else None

        return result


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


p = TreeNode(4)
q = TreeNode(5)
print(Solution().lowestCommonAncestor(root, p, q))
