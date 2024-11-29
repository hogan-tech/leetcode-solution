# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consec = 3
        for num in arr:
            if num % 2:
                consec -= 1
            else:
                consec = 3
            if consec == 0:
                return True
        return False


arr = [1, 1, 1]
print(Solution().threeConsecutiveOdds(arr))
