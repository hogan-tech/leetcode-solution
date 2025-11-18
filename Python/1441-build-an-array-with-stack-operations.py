#time complexity: O(n)
#space complexity: O(1)
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        idx = 0
        for item in target:
            while idx < item - 1:
                result.append("Push")
                result.append("Pop")
                idx += 1
            result.append("Push")
            idx += 1
        return result


target = [1, 3]
n = 3
print(Solution().buildArray(target, n))
target = [1, 2, 3]
n = 3
print(Solution().buildArray(target, n))
target = [1, 2]
n = 4
print(Solution().buildArray(target, n))
