# time complexity: O(n)
# space complexity: O(n)
from typing import Optional



class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = []
        index = 0
        n = len(traversal)

        while index < n:
            depth = 0
            while index < n and traversal[index] == '-':
                depth += 1
                index += 1
                
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
                
            node = TreeNode(value)

            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)

            if depth > 0:
                parent = levels[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        return levels[0]


traversal = "1-2--3--4-5--6--7"
print(Solution().recoverFromPreorder(traversal))
traversal = "1-2--3---4-5--6---7"
print(Solution().recoverFromPreorder(traversal))
traversal = "1-401--349---90--88"
print(Solution().recoverFromPreorder(traversal))
