# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(n):
            if n % (i + 1) == 0:
                k -= 1
            if k == 0:
                return i + 1
        return -1


n = 12
k = 3
print(Solution().kthFactor(n, k))
n = 7
k = 2
print(Solution().kthFactor(n, k))
n = 4
k = 4
print(Solution().kthFactor(n, k))
