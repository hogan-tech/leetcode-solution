# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n & 1:
                if n == 3 or (n >> 1) & 1 == 0:
                    n -= 1
                else:
                    n += 1
            else:
                n >>= 1
            count += 1
        return count


n = 8
print(Solution().integerReplacement(n))
n = 7
print(Solution().integerReplacement(n))
n = 4
print(Solution().integerReplacement(n))
n = 65535
print(Solution().integerReplacement(n))
