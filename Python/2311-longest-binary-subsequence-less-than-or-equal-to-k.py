# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        curSum = 0
        currLen = 0
        iMax = k.bit_length()
        for i, c in enumerate(s[::-1]):
            if c == "1":
                if i < iMax and curSum + (1 << i) <= k:
                    curSum += 1 << i
                    currLen += 1
            else:
                currLen += 1
        return currLen


s = "1001010"
k = 5
print(Solution().longestSubsequence(s, k))
s = "00101001"
k = 1
print(Solution().longestSubsequence(s, k))
