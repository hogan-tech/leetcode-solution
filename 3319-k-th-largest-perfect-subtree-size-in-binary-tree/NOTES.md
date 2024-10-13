​# Python | DFS | O(nlogn) | O(n)

## Overview
This code defines a binary tree and a function to find the size of the k-th largest perfect binary subtree within it. A perfect binary subtree is one where all leaf nodes are at the same level, and each parent node has exactly two children. Use dfs to get whole subtree.

## Time complexity: O(nlogn)
## Space complexity: O(n)

### TreeNode Class
The `TreeNode` class represents a node in a binary tree. It contains:
- **Attributes**:
  - `val`: The value of the node.
  - `left`: A reference to the left child node.
  - `right`: A reference to the right child node.

```python
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []

        def dfs(node):
            if not node:
                return True, 0, 0
            leftIsPerfect, leftHeight, leftSize = dfs(node.left)
            rightIsPerfect, rightHeight, rightSize = dfs(node.right)
            if leftIsPerfect and rightIsPerfect and leftHeight == rightHeight:
                currSize = leftSize + rightSize + 1
                sizes.append(currSize)
                return True, leftHeight + 1, currSize
            else:
                return False, 0, 0

        dfs(root)

        sizes.sort(reverse=True)

        if len(sizes) >= k:
            return sizes[k - 1]
        else:
            return -1
```
