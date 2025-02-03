# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinctNum = set(nums)
        for num in nums:
            newNum = int(str(num)[::-1])
            distinctNum.add(newNum)

        return len(distinctNum)


nums = [1, 13, 10, 12, 31]
print(Solution().countDistinctIntegers(nums))
nums = [2, 2, 2]
print(Solution().countDistinctIntegers(nums))
