# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt = 0
        maxAlt = currAlt
        for tempAlt in gain:
            currAlt += tempAlt
            maxAlt = max(maxAlt, currAlt)
        return maxAlt


gain = [-4, -3, -2, -1, 4, 3, 2]
print(Solution().largestAltitude(gain))
