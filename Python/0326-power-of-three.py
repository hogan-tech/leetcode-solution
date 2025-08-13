# time complexity: O(logn)
# space complexity: O(logn)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


n = 27
print(Solution().isPowerOfThree(n))
n = 0
print(Solution().isPowerOfThree(n))
n = -1
print(Solution().isPowerOfThree(n))
