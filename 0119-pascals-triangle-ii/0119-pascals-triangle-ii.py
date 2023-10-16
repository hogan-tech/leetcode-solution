from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for k in range(1, rowIndex+1):
            row.append(row[-1] * (rowIndex + 1 - k) // k)
        return row


print(Solution().getRow(5))
