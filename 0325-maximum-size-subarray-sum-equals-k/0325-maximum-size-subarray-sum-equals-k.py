class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        result = 0
        indices = {}
        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum == k:
                result = i + 1
            if prefixSum - k in indices:
                result = max(result, i - indices[prefixSum - k])
            if prefixSum not in indices:
                indices[prefixSum] = i
        return result