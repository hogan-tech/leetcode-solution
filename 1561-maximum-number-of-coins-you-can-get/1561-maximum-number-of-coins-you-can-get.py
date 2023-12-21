# time complexity: O(nlogn)
# space complexity: python timsort O(n) java c++ quicksort O(logn)
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        for i in range(len(piles)//3, len(piles), 2):
            ans += piles[i]
        return ans


piles = [2, 4, 1, 2, 7, 8]
print(Solution().maxCoins(piles))
