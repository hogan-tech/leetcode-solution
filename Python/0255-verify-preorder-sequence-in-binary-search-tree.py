# time complexity: O(n)
# space complexity: O(n)
from cmath import inf
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        minLimit = -inf
        stack = []
        for num in preorder:
            while stack and stack[-1] < num:
                minLimit = stack.pop()
            if num <= minLimit:
                return False
            stack.append(num)
        return True


preorder = [5, 2, 1, 3, 6]
print(Solution().verifyPreorder(preorder))
