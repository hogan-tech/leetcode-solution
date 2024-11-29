from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1]
            for k in range(1, i+1):
                row.append(row[-1] * (i + 1 - k) // k)
            res.append(row)
        return res


print(Solution().generate(5))
