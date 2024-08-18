# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        while n:
            if n % 2 == 0:
                n /= 2
                continue
            if n % 3 == 0:
                n /= 3
                continue
            if n % 5 == 0:
                n /= 5
                continue
            if n == 1:
                return True
            return False


n = 14
print(Solution().isUgly(n))
