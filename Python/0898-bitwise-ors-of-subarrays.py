# time complexity: O(nlogw)
# space complexity: O(nlogw)
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:

        result = set()
        curr = {0}
        for x in arr:
            curr = {x | y for y in curr} | {x}
            result |= curr
        return len(result)


arr = [0]
print(Solution().subarrayBitwiseORs(arr))
arr = [1, 1, 2]
print(Solution().subarrayBitwiseORs(arr))
arr = [1, 2, 4]
print(Solution().subarrayBitwiseORs(arr))
