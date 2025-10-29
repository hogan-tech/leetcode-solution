# time complexity: O(n^3)
# space complexity: O(n^2)
from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):
            if right - left < 0:
                return 0
            result = 0
            for i in range(left, right + 1):
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                remaining = dp(left, i - 1) + dp(i + 1, right)
                result = max(result, remaining + gain)
            return result

        return dp(1, len(nums) - 2)

# time complexity: O(n^3)
# space complexity: O(n^2)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                for i in range(left, right + 1):
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(remaining + gain, dp[left][right])
        
        return dp[1][n - 2]
'''
1. What is dp_state?
2. What does dp function return?
3. What is the base case?
4. How to calculate dp(dp_state) from dp(other_state)?

Psuedo code
function dp(dp_state, memo_dict) {
    // check if we have seen this dp_state
    if dp_state in memo_dict
        return memo_dict[dp_state]

    // base case (a case that we know the answer for already) such as dp_state is empty
    if dp_state is the base cases
        return things like 0 or null
    
    calculate dp(dp_state) from dp(other_state)
    
    save dp_state and the result into memo_dict
}

function answerToProblem(input) {
    return dp(start_state, empty_memo_dict)
}

DP(Naive)
// return maximum coins obtainable if we burst all balloons in `nums`.
function dp(nums, memo_dict) {
    // check if have we seen this dp_state
    if dp_state in memo_dict
        return memo_dict[dp_state]

    // base case
    if nums is empty
        return 0
    
    max_coins = 0
    for i in 1 ... nums.length - 2:
        // burst nums[i]
        gain = nums[i - 1] * nums[i] * nums[i + 1]
        // burst the remaining balloons
        remaining = dp(nums without nums[i])
        max_coins = max(max_coins, gain + remaining)
    
    save dp_state and the result into memo_dict
    return max_coins
}

function maxCoin(nums) {
    nums = [1] + nums + [1] // add fake balloons
    return dp(nums, empty_memo_dict)
}
'''

nums = [3, 1, 5, 8]
print(Solution().maxCoins(nums))
nums = [1, 5]
print(Solution().maxCoins(nums))
