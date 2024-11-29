# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstIdx = {}
        ans = -1
        for i in range(len(s)):
            if s[i] in firstIdx:
                ans = max(ans, i - firstIdx[s[i]] - 1)
            else:
                firstIdx[s[i]] = i
        return ans


s = "aba"
print(Solution().maxLengthBetweenEqualCharacters(s))
