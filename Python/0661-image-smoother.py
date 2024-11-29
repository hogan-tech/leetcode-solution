# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        smoothImg = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sum = 0
                count = 0
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y]
                            count += 1
                smoothImg[i][j] = sum // count
        return smoothImg


img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]

print(Solution().imageSmoother(img))
