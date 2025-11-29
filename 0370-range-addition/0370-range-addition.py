# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * (length + 1)
        for update in updates:
            result[update[0]] += update[2]
            result[update[1]+1] -= update[2]
        sum = 0
        for i, num in enumerate(result):
            sum += num
            result[i] = sum
        return result[:-1]


length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(Solution().getModifiedArray(length, updates))
length = 10
updates = [[2, 4, 6], [5, 6, 8], [1, 9, -4]]
print(Solution().getModifiedArray(length, updates))
