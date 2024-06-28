# time complexity: O(n)
# space complexity: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorderList = []
        self.Traversal(root, inorderList)

        return self.createBalancedBst(inorderList, 0, len(inorderList) - 1)

    def Traversal(self, root: TreeNode, inorder: list):
        if not root:
            return
        self.Traversal(root.left, inorder)
        inorder.append(root.val)
        self.Traversal(root.right, inorder)

    def createBalancedBst(self, inorder: list, start: int, end: int) -> TreeNode:
        if start > end:
            return None

        mid = start + (end - start) // 2

        leftSubtree = self.createBalancedBst(inorder, start, mid - 1)
        rightSubtree = self.createBalancedBst(inorder, mid + 1, end)

        node = TreeNode(inorder[mid], leftSubtree, rightSubtree)
        return node


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print(Solution().balanceBST(root))
