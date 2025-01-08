# time complexity: O(n)
# space complexity: O(logn)
from typing import List, Optional





class Solution:
    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        print(node.val, end=" ")
        self.traverse(node.left)
        self.traverse(node.right)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums: List[int], left: int, right: int):
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(nums, left, mid - 1)
            node.right = dfs(nums, mid + 1, right)
            return node
        
        return dfs(nums, 0, len(nums) - 1)


nums = [-10, -3, 0, 5, 9]
print(Solution().sortedArrayToBST(nums))
