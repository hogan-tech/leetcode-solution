# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 1
        for i in range(2, n + 1):
            total *= i
        result = 0
        while total % 10 == 0:
            result += 1
            total //= 10
        return result


n = 5
print(Solution().trailingZeroes(n))
