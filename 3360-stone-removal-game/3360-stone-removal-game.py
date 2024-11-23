# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def canAliceWin(self, n: int) -> bool:
        current = 10
        while n > 0:
            if n - current < 0:
                return current % 2 != 0
            n -= current
            current -= 1
        return current % 2 != 0


n = 19
print(Solution().canAliceWin(n))
n = 1
print(Solution().canAliceWin(n))
