# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total = sum(cost)
        keep = [0] * 26
        for ch, c in zip(s, cost):
            keep[ord(ch) - ord('a')] += c
        return total - max(keep)


s = "aabaac"
cost = [1, 2, 3, 4, 1, 10]
print(Solution().minCost(s, cost))
s = "abc"
cost = [10, 5, 8]
print(Solution().minCost(s, cost))
s = "zzzzz"
cost = [67, 67, 67, 67, 67]
print(Solution().minCost(s, cost))
