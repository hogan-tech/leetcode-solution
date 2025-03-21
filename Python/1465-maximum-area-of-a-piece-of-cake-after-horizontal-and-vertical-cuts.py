# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        verticalCuts.sort()
        horizontalCuts = [horizontalCuts[i] - horizontalCuts[i - 1]
                          for i in range(1, len(horizontalCuts))]
        verticalCuts = [verticalCuts[i] - verticalCuts[i - 1]
                        for i in range(1, len(verticalCuts))]
        return max(horizontalCuts) * max(verticalCuts) % MOD


h = 5
w = 4
horizontalCuts = [1, 2, 4]
verticalCuts = [1, 3]
print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
h = 5
w = 4
horizontalCuts = [3, 1]
verticalCuts = [1]
print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]
print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
h = 1000000000
w = 1000000000
horizontalCuts = [2]
verticalCuts = [2]
print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
