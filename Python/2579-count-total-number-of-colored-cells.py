# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * n * (n - 1) // 2


n = 1
print(Solution().coloredCells(n))
n = 2
print(Solution().coloredCells(n))
n = 3
print(Solution().coloredCells(n))

# 1 = 1 * 1 + 4 * 0
# 2 = 1 * 2 + 4 * 0 + 4 * 1
# 3 = 1 * 3 + 4 * 0 + 4 * 1 + 4 * 2
# 4 = 1 * 4 + 4 * 0 + 4 * 1 + 4 * 2 + 4 * 3
