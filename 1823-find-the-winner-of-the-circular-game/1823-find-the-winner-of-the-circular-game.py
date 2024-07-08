# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def solve(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (self.solve(n-1, k) + k) % n

    def findTheWinner(self, n: int, k: int) -> int:
        return self.solve(n, k) + 1


n = 5
k = 2

print(Solution().findTheWinner(n, k))
