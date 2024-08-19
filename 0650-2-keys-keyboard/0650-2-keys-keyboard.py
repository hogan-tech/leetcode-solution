# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n

        self.memo = [[0] * (n // 2 + 1) for _ in range(n + 1)]
        return 1 + self.minStepsHelper(1, 1)

    def minStepsHelper(self, currLen: int, pasteLen: int) -> int:
        if currLen == self.n:
            return 0
        if currLen > self.n:
            return 1000

        if self.memo[currLen][pasteLen] != 0:
            return self.memo[currLen][pasteLen]

        opt1 = 1 + self.minStepsHelper(currLen + pasteLen, pasteLen)
        opt2 = 2 + self.minStepsHelper(currLen * 2, currLen)
        self.memo[currLen][pasteLen] = min(opt1, opt2)
        return self.memo[currLen][pasteLen]


n = 3
print(Solution().minSteps(n))
