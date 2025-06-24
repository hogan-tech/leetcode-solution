from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        keyIdx = set()
        for i, num in enumerate(nums):
            if num == key:
                for targetIdx in range(i - k, i + k + 1):
                    if 0 <= targetIdx < n:
                        keyIdx.add(targetIdx)
            
        return list(keyIdx)


nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1
print(Solution().findKDistantIndices(nums, key, k))
nums = [2, 2, 2, 2, 2]
key = 2
k = 2
print(Solution().findKDistantIndices(nums, key, k))
