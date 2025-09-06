# time complexity: O(nlogR) let R be the maximum value of r across all intervals.
# space complexity: O(1)
from typing import List


class Solution:
    def get(self, num: int) -> int:
        i = 1
        base = 1
        count = 0
        while base <= num:
            count += ((i + 1) // 2) * (min(base * 2 - 1, num) - base + 1)
            i += 1
            base *= 2
        return count

    def minOperations(self, queries: List[List[int]]) -> int:
        result = 0
        for q in queries:
            result += (self.get(q[1]) - self.get(q[0] - 1) + 1) // 2
        return result


queries = [[1, 2], [2, 4]]
print(Solution().minOperations(queries))
queries = [[2,6]]
print(Solution().minOperations(queries))