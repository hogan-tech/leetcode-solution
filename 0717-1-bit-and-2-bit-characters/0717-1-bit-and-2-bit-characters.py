# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1


bits = [1, 0, 0]
print(Solution().isOneBitCharacter(bits))
bits = [1, 1, 1, 0]
print(Solution().isOneBitCharacter(bits))
