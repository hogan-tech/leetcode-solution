# time complexity: O(n+m)
# space complexity: O(1)
from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for num in left:
            ans = max(num, ans)
        for num in right:
            ans = max(n-num, ans)
        return ans


n = 7
left = []
right = [0, 1, 2, 3, 4, 5, 6, 7]


print(Solution().getLastMoment(n, left, right))
