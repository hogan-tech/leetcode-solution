# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroNums = [0 if num == 1 else 1 for num in nums]
        prefixLeft = [0 for _ in range(len(nums))]
        prefixLeft[0] = zeroNums[0]
        for i in range(1, len(zeroNums)):
            prefixLeft[i] = prefixLeft[i - 1] + zeroNums[i]
        prefixLeft.insert(0, 0)

        prefixRight = [0 for _ in range(len(nums) + 1)]
        prefixRight[-2] = nums[-1]
        for i in range(len(zeroNums) - 2, -1, -1):
            prefixRight[i] = prefixRight[i + 1] + nums[i]

        score = [prefixLeft[i] + prefixRight[i] for i in range(len(nums) + 1)]

        result = []
        maxScore = max(score)
        for i, num in enumerate(score):
            if num == maxScore:
                result.append(i)
        return result


nums = [0, 0, 1, 0]
print(Solution().maxScoreIndices(nums))
nums = [0, 0, 0]
print(Solution().maxScoreIndices(nums))
nums = [1, 1]
print(Solution().maxScoreIndices(nums))
