# time complexity: O(n)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num, feq in Counter(nums).most_common():
            if feq > 1:
                result.append(num)
        return result
    
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                result.append(num)
            nums[idx] *= -1
        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDuplicates(nums))
nums = [1,1,2]
print(Solution().findDuplicates(nums))
nums = [1]
print(Solution().findDuplicates(nums))
