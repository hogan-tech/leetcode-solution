# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rectangleMap = defaultdict(int)
        for x, y in rectangles:
            rectangleMap[x/y] += 1

        result = 0
        for val in rectangleMap.values():
            result += (1 + (val - 1)) * (val - 1) // 2
        return result


'''
1+2+3
4 * 3 / 2
'''

rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]
print(Solution().interchangeableRectangles(rectangles))
rectangles = [[4, 5], [7, 8]]
print(Solution().interchangeableRectangles(rectangles))
