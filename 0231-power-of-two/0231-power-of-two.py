# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1


n = 16
print(Solution().isPowerOfTwo(n))
