# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        result = []
        for i, (a, b, c, m) in enumerate(variables):
            if (a ** b % 10) ** c % m == target:
                result.append(i)
        return result


variables = [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]]
target = 2
print(Solution().getGoodIndices(variables, target))
variables = [[39, 3, 1000, 1000]]
target = 17
print(Solution().getGoodIndices(variables, target))
