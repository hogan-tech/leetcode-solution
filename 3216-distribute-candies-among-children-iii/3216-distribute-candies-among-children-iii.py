

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def cal(num: int):
            if num < 0:
                return 0
            return num * (num - 1) // 2
        return cal(n + 2) - 3 * cal(n - limit + 1) + 3 * cal(n - (limit + 1) * 2 + 2) - cal(n - 3 * (limit + 1) + 2)


n = 5
limit = 2
print(Solution().distributeCandies(n, limit))
n = 3
limit = 3
print(Solution().distributeCandies(n, limit))
