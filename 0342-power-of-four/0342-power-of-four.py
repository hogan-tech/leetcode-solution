class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while (n >= 1.0):
            if (n == 1.0):
                return True
            n /= 4

        return False


print(Solution().isPowerOfFour(64))
