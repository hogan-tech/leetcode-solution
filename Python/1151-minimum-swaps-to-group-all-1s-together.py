# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        onesTotal = sum(data)
        left, right = 0, 0
        countOne, maxOne = 0, 0
        while right < len(data):
            countOne += data[right]
            right += 1
            if right - left > onesTotal:
                countOne -= data[left]
                left += 1
            maxOne = max(maxOne, countOne)
        return onesTotal - maxOne


data = [1, 0, 1, 0, 1]
print(Solution().minSwaps(data))
