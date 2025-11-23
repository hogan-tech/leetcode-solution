# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def helper(x: int) -> int:
            s = str(x)
            if len(s) < 3:
                return 0
            w = 0
            for i in range(1, len(s)-1):
                a, b, c = int(s[i-1]), int(s[i]), int(s[i+1])
                if b > a and b > c:
                    w += 1
                elif b < a and b < c:
                    w += 1
            return w
        total = 0
        for n in range(num1, num2 + 1):
            total += helper(n)
        return total


num1 = 120
num2 = 130
print(Solution().totalWaviness(num1, num2))
num1 = 198
num2 = 202
print(Solution().totalWaviness(num1, num2))
num1 = 4848
num2 = 4848
print(Solution().totalWaviness(num1, num2))
