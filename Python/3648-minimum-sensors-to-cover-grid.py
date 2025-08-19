# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        span = 2*k + 1
        rows = (n + span - 1) // span
        cols = (m + span - 1) // span
        return rows * cols


n = 5
m = 5
k = 1
print(Solution().minSensors(n, m, k))
n = 2
m = 2
k = 2
print(Solution().minSensors(n, m, k))
