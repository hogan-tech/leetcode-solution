class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        right, left = self.invertTree(root.right), self.invertTree(root.left)
        root.left, root.right = right, left
        return root