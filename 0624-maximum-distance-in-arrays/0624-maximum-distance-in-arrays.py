from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        size = len(arrays[0])
        res = 0
        minNum = arrays[0][0]
        maxNum = arrays[0][size - 1]
        for i in range(1, len(arrays)):
            size = len(arrays[i])
            res = max(
                res, max(abs(arrays[i][size-1] - minNum), abs(maxNum - arrays[i][0])))
            minNum = min(arrays[i][0], minNum)
            maxNum = max(arrays[i][size - 1], maxNum)
        return res


arrays = [[1, 4], [0, 5]]
print(Solution().maxDistance(arrays))
