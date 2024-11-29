# time complexity:O(nlogn)
# space complexity: O(n)
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numStr = list(map(str, nums))

        def compareHelper(x, y) -> bool:
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        numStr.sort(key=cmp_to_key(compareHelper))
        return '0' if "".join(numStr)[0] == '0' else "".join(numStr)


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
