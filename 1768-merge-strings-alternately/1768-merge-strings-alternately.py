class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        ans = ""
        for i in range(minLen):
            ans += word1[i]
            ans += word2[i]
        if len(word1) > minLen:
            ans += word1[minLen:]
        if len(word2) > minLen:
            ans += word2[minLen:]
        return ans


word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2))
