# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        base = sum(technique2)
        gains = [technique1[i] - technique2[i] for i in range(n)]

        gains.sort(reverse=True)
        total = base + sum(gains[:k])
        for g in gains[k:]:
            if g > 0:
                total += g
        return total


technique1 = [5, 2, 10]
technique2 = [10, 3, 8]
k = 2
print(Solution().maxPoints(technique1, technique2, k))
technique1 = [10, 20, 30]
technique2 = [5, 15, 25]
k = 2
print(Solution().maxPoints(technique1, technique2, k))
technique1 = [1, 2, 3]
technique2 = [4, 5, 6]
k = 0
print(Solution().maxPoints(technique1, technique2, k))
