from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans = 0
        pairs.sort(key=lambda x: x[1])
        curr = float('-inf')
        for i in range(len(pairs)):
            if pairs[i][0] > curr:
                ans += 1
                curr = pairs[i][1]
        return ans


pairs = [[1, 2], [2, 3], [3, 4]]
print(Solution().findLongestChain(pairs))
