# time complexity: O(n^2)
# space complexity: O(n)
from collections import defaultdict
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            radiant = defaultdict(int)
            for j in range(n):
                if j != i:
                    radiant[math.atan2(
                        points[j][1] - points[i][1],
                        points[j][0] - points[i][0]
                    )] += 1
            result = max(result, max(radiant.values()) + 1)
        return result


points = [[1, 1], [2, 2], [3, 3]]
print(Solution().maxPoints(points))
