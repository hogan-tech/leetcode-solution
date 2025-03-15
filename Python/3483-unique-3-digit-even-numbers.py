# time complexity: O(1)
# space complexity: O(1)
from itertools import permutations
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numSet = set()
        for num in permutations(digits, 3):
            if num[0] == 0:
                continue
            if num[2] % 2 != 0:
                continue
            number = num[0] * 100 + num[1]*10 + num[2]
            numSet.add(number)
        return len(numSet)


digits = [1, 2, 3, 4]
print(Solution().totalNumbers(digits))
digits = [0, 2, 2]
print(Solution().totalNumbers(digits))
digits = [6, 6, 6]
print(Solution().totalNumbers(digits))
digits = [1, 3, 5]
print(Solution().totalNumbers(digits))
