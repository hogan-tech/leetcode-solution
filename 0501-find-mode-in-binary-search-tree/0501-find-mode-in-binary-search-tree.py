from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node: Optional[TreeNode], counter):
            if not node:
                return
            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)

        counter = defaultdict(int)
        dfs(root, counter)
        res = []
        maxFrequencies = max(counter.values())

        for key in counter:
            if maxFrequencies == counter[key]:
                res.append(key)

        return res


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)


print(Solution().findMode(root))
