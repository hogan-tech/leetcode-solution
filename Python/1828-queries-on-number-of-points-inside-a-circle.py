# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for query in queries:
            origX, origY, r = query
            count = 0
            for x, y in points:
                if (origX - x) ** 2 + (origY - y) ** 2 <= r ** 2:
                    count += 1
            result.append(count)
        return result


points = [[1, 3], [3, 3], [5, 3], [2, 2]]
queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
print(Solution().countPoints(points, queries))
points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
print(Solution().countPoints(points, queries))
