# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ROW = len(image)
        mid = (ROW + 1) // 2
        for r in range(ROW):
            for i in range(mid):
                temp = image[r][i] ^ 1
                image[r][i] = image[r][ROW - 1 - i] ^ 1
                image[r][ROW - 1 - i] = temp
        return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(Solution().flipAndInvertImage(image))
image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
print(Solution().flipAndInvertImage(image))
