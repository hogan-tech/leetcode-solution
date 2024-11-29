#time complexity: O(n)
#space complexity: O(1)

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        index = 0
        for item in target:
            while index < item - 1:
                res.append("Push")
                res.append("Pop")
                index += 1
            res.append("Push")
            index += 1
        return res


target = [1, 3]
n = 3


print(Solution().buildArray(target, n))
