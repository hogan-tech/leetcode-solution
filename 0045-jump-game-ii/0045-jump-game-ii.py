from typing import List

# Backtracking
# O(2^n) - Times out
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = float('inf')
        
        def backtrack(candidate, end):
            if candidate >= result:
                return
            if end <= 0:
                result = candidate
            for i in range(end)[::-1]:
                if nums[i] + i >= end:
                    backtrack(candidate + 1, i)

        backtrack(0, len(nums)-1)
        return result

# Memoized backtracking (Top-down DP)
# O(n^2) - Times out
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = float('inf')
        memo = {}
        def backtrack(candidate, end):
            if (candidate, end) in memo:
                return memo[candidate, end]
            if candidate >= result:
                return
            if end <= 0:
                result = candidate
            for i in range(end)[::-1]:
                if nums[i] + i >= end:
                    backtrack(candidate + 1, i)

            memo[(candidate, end)] = result
            return memo[(candidate, end)]

        backtrack(0, len(nums)-1)
        return result

# Bottom-Up DP
# O(nm) 
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        dp = [0]
        for i in range(len(nums)):
            dp.append(max((nums[j]+j for j in range(dp[i]+1))))
            if dp[i+1] >= len(nums)-1:
                break
        return len(dp) - 1
    
# Greedy
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        last = next = 0
        count = 1
        for _ in range(len(nums)):
            temp = next
            next = max(nums[j] + j for j in range(last, next + 1))
            if next >= len(nums) - 1:
                break
            count += 1
            last = temp
        return count
    
    
nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))
nums = [2, 3, 0, 1, 4]
print(Solution().jump(nums))
