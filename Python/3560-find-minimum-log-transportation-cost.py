# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0
        x = max(n, m)
        return k * (x - k)


n = 6
m = 5
k = 5
print(Solution().minCuttingCost(n, m, k))
n = 4
m = 4
k = 6
print(Solution().minCuttingCost(n, m, k))
