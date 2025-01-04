# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i

        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            ans += len(between)
        return ans


s = "aabca"
print(Solution().countPalindromicSubsequence(s))
s = "adc"
print(Solution().countPalindromicSubsequence(s))
s = "bbcbaba"
print(Solution().countPalindromicSubsequence(s))
