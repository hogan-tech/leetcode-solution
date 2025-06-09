# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addToArr(self, node: Optional[TreeNode], treeList: List[int]) -> None:
        if node:
            self.addToArr(node.left, treeList)
            treeList.append(node.val)
            self.addToArr(node.right, treeList)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.addToArr(root, result)
        return result[k-1]

# time complexity: O(H)
# space complexity: O(H)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1

            if k == 0:
                return root.val
            
            root = root.right


root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)
print(Solution().kthSmallest(root, 1))
