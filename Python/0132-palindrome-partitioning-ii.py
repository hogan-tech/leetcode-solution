# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cutsDP = [0 for _ in range(n)]
        dp = [[False for _ in range(n)] for _ in range(n)]

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True

        for right in range(len(s)):
            minimumCut = right
            for left in range(right + 1):
                if dp[left][right]:
                    if left == 0:
                        minimumCut = 0
                    else:
                        minimumCut = min(minimumCut, cutsDP[left - 1] + 1)
            cutsDP[right] = minimumCut
        return cutsDP[len(s) - 1]

# time complexity: O(n^2 * n)
# space complexity: O(n^2)
class Solution:
    def __init__(self):
        self.memoCuts = []
        self.memoPalindrome = []

    def minCut(self, s: str) -> int:
        self.memoCuts = [[None] * len(s) for _ in range(len(s))]
        self.memoPalindrome = [[None] * len(s) for _ in range(len(s))]
        return self.findMinimumCut(s, 0, len(s) - 1, len(s) - 1)

    def findMinimumCut(self, s, start, end, minimumCut):
        if start == end or self.isPalindrome(s, start, end):
            return 0
        if self.memoCuts[start][end] != None:
            return self.memoCuts[start][end]
        for currentEndIndex in range(start, end + 1):
            if self.isPalindrome(s, start, currentEndIndex):
                minimumCut = min(
                    minimumCut,
                    1
                    + self.findMinimumCut(
                        s, currentEndIndex + 1, end, minimumCut
                    ),
                )
        self.memoCuts[start][end] = minimumCut
        return self.memoCuts[start][end]

    def isPalindrome(self, s, start, end):
        if start >= end:
            return True
        if self.memoPalindrome[start][end] != None:
            return self.memoPalindrome[start][end]
        self.memoPalindrome[start][end] = (
            s[start] == s[end]) and self.isPalindrome(s, start + 1, end - 1)
        return self.memoPalindrome[start][end]


s = "aab"
print(Solution().minCut(s))
s = "a"
print(Solution().minCut(s))
s = "ab"
print(Solution().minCut(s))
