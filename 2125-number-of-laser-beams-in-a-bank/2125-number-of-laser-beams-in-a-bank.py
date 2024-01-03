# time complexity: O(m * n)
# space complexity: O(1)
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        laserSum = 0
        for row in bank:
            if row.count('1'):
                laserSum += prev * row.count('1')
                prev = row.count('1')
        return laserSum


bank = ["011001", "000000", "010100", "001000"]
print(Solution().numberOfBeams(bank))
