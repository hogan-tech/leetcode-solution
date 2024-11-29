# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        stack = []

        dp = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                previousSmaller = stack[-1]
                dp[i] = dp[previousSmaller] + (i - previousSmaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            stack.append(i)

        return sum(dp) % MOD


arr = [3, 1, 2, 4]

print(Solution().sumSubarrayMins(arr))
