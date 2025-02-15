# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            idx = 1
            while idx < len(n) and str(x) >= n[idx]:
                idx += 1
        else:
            idx = 0
            while idx < len(n) and str(x) <= n[idx]:
                idx += 1

        return n[:idx] + str(x) + n[idx:]


n = "99"
x = 9
print(Solution().maxValue(n, x))
n = "-13"
x = 2
print(Solution().maxValue(n, x))
n = "73"
x = 6
print(Solution().maxValue(n, x))
