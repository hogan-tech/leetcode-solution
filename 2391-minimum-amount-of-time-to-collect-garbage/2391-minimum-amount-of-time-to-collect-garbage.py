# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        ans = 0
        for i in range(n - 1):
            ans += 3 * travel[i]
        for s in garbage:
            ans += len(s)
        for i in range(n - 1, 0, -1):
            if "G" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break
        for i in range(n - 1, 0, -1):
            if "P" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break
        for i in range(n - 1, 0, -1):
            if "M" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break
        return ans


garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]
print(Solution().garbageCollection(garbage, travel))
