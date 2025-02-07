# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.insert(0, bottom)
        special.append(top)
        special.sort()
        maxNum = 0
        for i in range(1, len(special)):
            if i == 1 or i == len(special) - 1:
                maxNum = max(maxNum, special[i] - special[i - 1])
            else:
                maxNum = max(maxNum, special[i] - special[i - 1] - 1)
        return maxNum


bottom = 2
top = 9
special = [4, 6]
print(Solution().maxConsecutive(bottom, top, special))
bottom = 6
top = 8
special = [7, 6, 8]
print(Solution().maxConsecutive(bottom, top, special))
