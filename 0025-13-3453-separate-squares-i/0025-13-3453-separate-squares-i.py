# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calculate(y):
            above = 0
            below = 0
            for x, yS, l in squares:
                yTop = yS + l
                if yTop <= y:
                    below += l ** 2
                elif yS >= y:
                    above += l ** 2
                else:
                    overlap = y - yS
                    below += overlap * l
                    above += (l - overlap) * l
            return above, below

        minY = float('inf')
        maxY = float('-inf')
        for x, yS, l in squares:
            minY = min(minY, yS)
            maxY = max(maxY, yS + l)

        precision = 1e-5
        left = minY
        right = maxY
        while right - left > precision:
            mid = (left + right) / 2
            above, below = calculate(mid)
            if above > below:
                left = mid
            else:
                right = mid
        return (left + right) / 2


squares = [[0, 0, 1], [2, 2, 1]]
print(Solution().separateSquares(squares))
squares = [[0, 0, 2], [1, 1, 1]]
print(Solution().separateSquares(squares))
'''
below = (y - ay1) * al + (y - by1) * bl
upper = (ay1 + al - y) * al + (by1 + bl - y) * bl

(0, 0) (2, 2) y ->
(1, 1) (2, 2) y ->
'''
