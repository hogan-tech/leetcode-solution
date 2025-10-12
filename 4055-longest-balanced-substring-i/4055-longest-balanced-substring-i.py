# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxLen = 0

        for left in range(n):
            freq = [0] * 26
            for right in range(left, n):
                freq[ord(s[right]) - ord('a')] += 1
                nonzero = [f for f in freq if f > 0]
                if len(set(nonzero)) == 1:
                    maxLen = max(maxLen, right - left + 1)
        return maxLen


s = "abbac"
print(Solution().longestBalanced(s))
s = "zzabccy"
print(Solution().longestBalanced(s))
s = "aba"
print(Solution().longestBalanced(s))
