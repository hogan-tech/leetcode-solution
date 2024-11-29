# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        originalHiehgt = heights
        expectedHeight = []
        for i in range(len(heights)):
            expectedHeight.append(heights[i])
        count = 0
        expectedHeight.sort()
        print(originalHiehgt)
        for i in range(len(heights)):
            if originalHiehgt[i] != expectedHeight[i]:
                count += 1
        return count


heights = [1, 1, 4, 2, 1, 3]
print(Solution().heightChecker(heights))
