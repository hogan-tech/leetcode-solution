# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        nBytes = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            mask = 1 << 7
            if nBytes == 0:
                while mask & num:
                    nBytes += 1
                    mask = mask >> 1
                if nBytes == 0:
                    continue
                if nBytes == 1 or nBytes > 4:
                    return False
            else:
                if not (num & mask1 and not (num & mask2)):
                    return False
            nBytes -= 1
        return nBytes == 0


data = [197, 130, 1]
print(Solution().validUtf8(data))
data = [235, 140, 4]
print(Solution().validUtf8(data))
