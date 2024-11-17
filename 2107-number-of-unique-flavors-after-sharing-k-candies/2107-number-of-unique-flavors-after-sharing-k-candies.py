# time complexity: O(n)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        result = 0
        candyCounter = Counter(candies)
        for i, key in enumerate(candies):
            candyCounter[key] -= 1
            if candyCounter[key] == 0:
                del candyCounter[key]
            if i >= k:
                candyCounter[candies[i-k]] += 1
            if i >= k - 1:
                result = max(result, len(candyCounter))
        return result


candies = [1, 2, 2, 3, 4, 3]
k = 3
print(Solution().shareCandies(candies, k))
candies = [2, 2, 2, 2, 3, 3]
k = 2
print(Solution().shareCandies(candies, k))
candies = [2, 4, 5]
k = 0
print(Solution().shareCandies(candies, k))
