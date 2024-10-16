from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        runs = {}
        best = [0] * (k + 1)
        for x in nums:
            if x not in runs:
                runs[x] = [1] * (k + 1)
            else:
                runs[x] = [z + 1 for z in runs[x]]
            runs[x][1:] = [max(otherrun + 1, xrun)
                           for otherrun, xrun in zip(best, runs[x][1:])]
            best = [max(b, xrun) for b, xrun in zip(best, runs[x])]
        return max(best)


nums = [1, 2, 1, 1, 3]
k = 2
print(Solution().maximumLength(nums, k))
