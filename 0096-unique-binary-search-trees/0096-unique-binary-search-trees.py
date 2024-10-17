# time complexity: O(n)
# space complexity: O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
      r  
    /    \
1~r-1   r+1~n
'''


class Solution:
    def numTrees(self, n: int) -> int:
        T = {}
        T[0], T[1] = 1, 1
        for k in range(2, n + 1):
            T[k] = sum([T[r-1] * T[k - r] for r in range(1, k + 1)])
        print(T)
        return T[n]


print(Solution().numTrees(3))
