# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW = len(image)
        COL = len(image[0])

        queue = deque()
        visited = set()
        queue.append((sr, sc))
        visited.add((sr, sc))
        originalColor = image[sr][sc]
        while queue:
            currR, currC = queue.popleft()
            if image[currR][currC] != color:
                image[currR][currC] = color

            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and (nextR, nextC) not in visited:
                    if image[nextR][nextC] == originalColor:
                        queue.append((nextR, nextC))
                        visited.add((nextR, nextC))
        
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(Solution().floodFill(image, sr, sc, color))
image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
print(Solution().floodFill(image, sr, sc, color))
