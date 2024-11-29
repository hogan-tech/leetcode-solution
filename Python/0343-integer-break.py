from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        @cache 
        def dp(num):
            if num <= 3:
                return num
            ans = num
            for i in range(2, num):
                ans = max(ans, i*dp(num-i))
            return ans
        if n <= 3:
            return n - 1
        return dp(n)