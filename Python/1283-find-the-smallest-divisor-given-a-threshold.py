# time complexity: O(nlogn)
# space complexity: O(1)
from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def findDivisionSum(divisor: int) -> int:
            count = 0
            for num in nums:
                count += ceil((1.0 * num) / divisor)
            return count
        
        result = -1
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if findDivisionSum(mid) <= threshold:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result


'''
9 + 5 + 7 + 3 + 1
'''

nums = [1, 2, 5, 9]
threshold = 6
print(Solution().smallestDivisor(nums, threshold))
nums = [44, 22, 33, 11, 1]
threshold = 5
print(Solution().smallestDivisor(nums, threshold))
