# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])

        checkForZero = original[0] == original[-1]
        original = [1]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        checkForOne = original[0] == original[-1]

        return checkForZero or checkForOne


derived = [1, 1, 0]
print(Solution().doesValidArrayExist(derived))
derived = [1, 1]
print(Solution().doesValidArrayExist(derived))
derived = [1, 0]
print(Solution().doesValidArrayExist(derived))
