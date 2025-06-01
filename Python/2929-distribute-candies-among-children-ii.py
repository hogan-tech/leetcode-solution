# time complexity: O(min(limit, n))
# space complexity: O(1)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            result += min(n - i, limit) - max(0, n - i - limit) + 1
        return result


n = 5
limit = 2
print(Solution().distributeCandies(n, limit))
n = 3
limit = 3
print(Solution().distributeCandies(n, limit))
