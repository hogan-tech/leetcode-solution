from typing import Counter, List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = [(key, val) for key, val in Counter(nums).items()]
        freq.sort()
        result = 0
        for i in range(len(freq) - 1):
            if freq[i + 1][0] - freq[i][0] == 1:
                result = max(result, freq[i][1] + freq[i + 1][1])

        return result


nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(Solution().findLHS(nums))
nums = [1, 2, 3, 4]
print(Solution().findLHS(nums))
nums = [1, 1, 1, 1]
print(Solution().findLHS(nums))
