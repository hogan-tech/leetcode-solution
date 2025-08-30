# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n * m) // 2


n = 3
m = 2
print(Solution().flowerGame(n, m))
n = 1
m = 1
print(Solution().flowerGame(n, m))
