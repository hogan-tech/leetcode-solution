# time complexity: O((n+m)log(m+n))
# space complexity: O(m+n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node: Optional[TreeNode]):
            if node is None:
                return
            result.append(node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        traverse(root1)
        traverse(root2)
        
        return sorted(result)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)
print(Solution().getAllElements(root1, root2))
