from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        freq = defaultdict(int)
        currSum = 0
        result = 0
        for i in range(k):
            freq[nums[i]] += 1
            currSum += nums[i]
        if len(freq) >= m:
            result = max(result, currSum)
        
        for i in range(len(nums) - k):
            leftNum = nums[i]
            rightNum = nums[i + k]
            freq[leftNum] -= 1
            currSum -= leftNum
            freq[rightNum] += 1
            currSum += rightNum
            if freq[leftNum] == 0:
                del freq[leftNum]
            if len(freq) >= m:
                result = max(result, currSum)
                
        return result

'''
2 6 7 3

  6 7 3 1

    7 3 1 7
'''
nums = [2, 6, 7, 3, 1, 7]
m = 3
k = 4
print(Solution().maxSum(nums, m, k))
nums = [5, 9, 9, 2, 4, 5, 4]
m = 1
k = 3
print(Solution().maxSum(nums, m, k))
nums = [1, 2, 1, 2, 1, 2, 1]
m = 3
k = 3
print(Solution().maxSum(nums, m, k))
