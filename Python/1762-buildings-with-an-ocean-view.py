# time complexity: O(n)
# space compelxity: O(n)
from collections import deque
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = 0
        queue = deque()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxHeight:
                queue.appendleft(i)
                maxHeight = heights[i]
        return list(queue)


heights = [4, 2, 3, 1]
print(Solution().findBuildings(heights))
heights = [4, 3, 2, 1]
print(Solution().findBuildings(heights))
heights = [1, 3, 2, 4]
print(Solution().findBuildings(heights))
