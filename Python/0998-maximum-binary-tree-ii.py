# time complexity: O(n)
# space complexity: O(n)
from typing import Optional




class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node


root1 = TreeNode(4)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
root1.right.left = TreeNode(2)
val = 5
print(Solution().insertIntoMaxTree(root1, val))
root2 = TreeNode(5)
root2.left = TreeNode(2)
root2.right = TreeNode(4)
root2.left.right = TreeNode(1)
val = 3
print(Solution().insertIntoMaxTree(root2, val))
root3 = TreeNode(5)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.right = TreeNode(1)
val = 4
print(Solution().insertIntoMaxTree(root3, val))
