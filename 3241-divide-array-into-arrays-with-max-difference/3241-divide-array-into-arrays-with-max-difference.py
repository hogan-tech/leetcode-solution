from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if (nums[i+2] - nums[i] > k):
                return []
            ans.append([nums[i], nums[i+1], nums[i+2]])
        return ans


nums = [1, 3, 4, 8, 7, 11, 3, 5, 1]
k = 2
print(Solution().divideArray(nums, k))
