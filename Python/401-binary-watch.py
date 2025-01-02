# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hr in range(12):
            for min in range(60):
                if bin(hr).count('1') + bin(min).count('1') == turnedOn:
                    result.append(f"{hr}:{min:02}")
        return result


turnedOn = 1
print(Solution().readBinaryWatch(turnedOn))
turnedOn = 9
print(Solution().readBinaryWatch(turnedOn))
