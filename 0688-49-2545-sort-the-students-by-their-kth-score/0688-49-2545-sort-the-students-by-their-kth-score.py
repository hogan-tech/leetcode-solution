# time complexity: O(nlogn)
# space complexity: O(n^2)
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        scoreRow = []
        ROW = len(score)
        for r in range(ROW):
            scoreRow.append((score[r][k], r))
        scoreRow.sort(reverse=True)
        result = []
        for r in range(ROW):
            currStudent = scoreRow[r][1]
            result.append(score[currStudent])

        return result


score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
k = 2
print(Solution().sortTheStudents(score, k))
score = [[3, 4], [5, 6]]
k = 0
print(Solution().sortTheStudents(score, k))
