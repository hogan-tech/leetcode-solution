# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorDict = defaultdict(list)
        ballDict = defaultdict(int)
        result = []
        for ball, color in queries:
            if ball in ballDict:
                prevColor = ballDict[ball]
                colorDict[prevColor].remove(ball)
                if not colorDict[prevColor]:
                    del colorDict[prevColor]
                ballDict[ball] = color
                colorDict[color].append(ball)
            else:
                ballDict[ball] = color
                colorDict[color].append(ball)
            result.append(len(colorDict))
        return result


limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
print(Solution().queryResults(limit, queries))
limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
print(Solution().queryResults(limit, queries))
