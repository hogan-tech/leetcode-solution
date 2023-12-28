from functools import lru_cache


class Solution:
	def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
		@lru_cache(None)
		def dp(idx, lastChar, lastCharCount, k):
			if k < 0: 
				return float('inf')
			if idx == n: 
				return 0
			deleteChar = dp(idx + 1, lastChar, lastCharCount, k - 1)
			if s[idx] == lastChar:
				keepChar = dp(idx + 1, lastChar, lastCharCount + 1, k) + (lastCharCount in [1, 9, 99])
			else:
				keepChar = dp(idx + 1, s[idx], 1, k) + 1
			return min(keepChar, deleteChar)
		n = len(s)
		return dp(0, "", 0, k)

s = "aaabcccd"
k = 2

print(Solution().getLengthOfOptimalCompression(s, k))
