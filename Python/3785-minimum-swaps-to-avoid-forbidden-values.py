# time complexity: O(n)
# space complexity: O(n)
from typing import List
from collections import Counter

class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        counterNum = Counter(nums)
        counterForbidden = Counter(forbidden)
        
        for v in counterNum:
            if counterNum[v] > (n - counterForbidden[v]):
                return -1
        
        badList = [nums[i] for i in range(n) if nums[i] == forbidden[i]]
        k = len(badList)
        if k == 0:
            return 0
            
        counterBadVal = Counter(badList)
        maxBadFreq = max(counterBadVal.values())
        
        return max((k + 1) // 2, maxBadFreq)



nums = [1, 2, 3]
forbidden = [3, 2, 1]
print(Solution().minSwaps(nums, forbidden))
nums = [4, 6, 6, 5]
forbidden = [4, 6, 5, 5]
print(Solution().minSwaps(nums, forbidden))
nums = [7, 7]
forbidden = [8, 7]
print(Solution().minSwaps(nums, forbidden))
nums = [1, 2]
forbidden = [2, 1]
print(Solution().minSwaps(nums, forbidden))
