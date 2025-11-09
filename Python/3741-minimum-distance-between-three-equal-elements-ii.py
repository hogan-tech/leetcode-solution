# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashMap = defaultdict(list)
        for i, num in enumerate(nums):
            hashMap[num].append(i)
        result = float('inf')
        
        for idxs in hashMap.values():
            if len(idxs) >= 3:
                for i in range(len(idxs) - 2):
                    dist = 2 * (idxs[i + 2] - idxs[i])
                    result = min(result, dist)
        return result if result != float('inf') else -1



nums = [1, 2, 1, 1, 3]
print(Solution().minimumDistance(nums))
nums = [1, 1, 2, 3, 2, 1, 2]
print(Solution().minimumDistance(nums))
nums = [1]
print(Solution().minimumDistance(nums))
