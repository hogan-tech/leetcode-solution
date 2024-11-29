# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sampleString = "123456789"
        maxIdx = 10
        ans = []
        for i in range(len(str(low)), len(str(high))+1):
            for start in range(maxIdx - i):
                tempNum = int(sampleString[start: start + i])
                if tempNum >= low and tempNum <= high:
                    ans.append(tempNum)
        return ans


low = 100
high = 300
print(Solution().sequentialDigits(low, high))
