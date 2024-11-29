# time complexity: O(n)
# space complexity: O(n)
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frequency = [0] * (len(nums) + 1)
        res = [[]]
        for i in nums:
            if frequency[i] >= len(res):
                res.append([])
            res[frequency[i]].append(i)
            frequency[i] += 1
        return res

nums = [1, 3, 4, 1, 2, 3, 1]
print(Solution().findMatrix(nums))
