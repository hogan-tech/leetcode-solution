# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        COL = len(colsum)
        ROW = 2
        result = [[0 for _ in range(COL)] for _ in range(ROW)]
        for i in range(COL):
            if colsum[i] == 2:
                if upper > 0 and lower > 0:
                    result[0][i] = 1
                    result[1][i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []

        for i in range(COL):
            if colsum[i] == 1:
                if upper > 0:
                    result[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    result[1][i] = 1
                    lower -= 1
                elif upper == 0 and lower == 0:
                    return []
        if upper or lower:
            return []
        return result


'''
[1, 1, 1, 0, 1, 0, 0, 1, 0, 0]
[1, 0, 1, 0, 0, 0, 1, 1, 0, 1]

[1,1,1,0,1,0,0,1,0,0]
[1,0,1,0,0,0,1,1,0,1]
'''
upper = 5
lower = 5
colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]
print(Solution().reconstructMatrix(upper, lower, colsum))
upper = 2
lower = 1
colsum = [1, 1, 1]
print(Solution().reconstructMatrix(upper, lower, colsum))
upper = 2
lower = 3
colsum = [2, 2, 1, 1]
print(Solution().reconstructMatrix(upper, lower, colsum))
