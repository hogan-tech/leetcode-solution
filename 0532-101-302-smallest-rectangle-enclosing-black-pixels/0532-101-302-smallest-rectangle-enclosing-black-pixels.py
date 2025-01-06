# time complexity: O(nlogm) + O(mlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:

        ROW = len(image)
        COL = len(image[0])

        def binarySearch(low: int, high: int, checkFunc):
            left = low
            right = high
            while left < right:
                mid = left + (right - left) // 2
                if checkFunc(mid):
                    right = mid
                else:
                    left = mid + 1
            return left

        def containsInCol(mid: int):
            return any(image[i][mid] == '1' for i in range(len(image)))

        def containsInRow(mid: int):
            return '1' in image[mid]

        left = binarySearch(0, y, containsInCol)
        right = binarySearch(
            y + 1, COL, lambda mid: not containsInCol(mid)) - 1
        top = binarySearch(0, x, containsInRow)
        bottom = binarySearch(x+1, ROW, lambda mid: not containsInRow(mid)) - 1
        return (right - left + 1) * (bottom - top + 1)


image = [["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]]
x = 0
y = 2
print(Solution().minArea(image, x, y))
image = [["1"]]
x = 0
y = 0
print(Solution().minArea(image, x, y))
