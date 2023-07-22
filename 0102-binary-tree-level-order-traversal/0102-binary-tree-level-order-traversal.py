class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels: List[List[int]] = []
        if not root:
            return levels

        def helper(node: TreeNode, level: List[int]):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root,0)
    
        return levels