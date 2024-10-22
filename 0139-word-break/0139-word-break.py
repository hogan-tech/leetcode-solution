# Tries
# time complexity: O(n^2 + m*k)
# space complexity: O(n + m*k)
from typing import List


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isWord = True

        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i-1]:
                curr = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in curr.children:
                        break
                    curr = curr.children[c]
                    if curr.isWord:
                        dp[j] = True
        return dp[-1]

# DP 2
# time complexity: O(n^3 +m*k)
# space complexity: O(n+m*k)
# from typing import List
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         sLen = len(s)
#         words = set(wordDict)
#         dp = [False] * (sLen + 1)
#         dp[0] = True
#         for i in range(1, sLen + 1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in words:
#                     dp[i] = True
#                     break
#         return True


# DP 1
# time complexity: O(n*m*k)
# space complexity: O(n)
#
# from typing import List
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         sLen = len(s)
#         dp = [False] * sLen
#         for i in range(sLen):
#             for word in wordDict:
#                 wordLen = len(word)
#                 if i < wordLen - 1:
#                     continue
#                 if i == wordLen - 1 or dp[i-wordLen]:
#                     if s[i-wordLen+1:i + 1] == word:
#                         dp[i] = True
#                         break
#         print(dp)
#         return dp[sLen-1]


# BFS
# time complexity: O(n^3 + m*k)
# space complexity: O(n+m*k)
#
# from collections import deque
# from typing import List
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words = set(wordDict)
#         queue = deque([0])
#         seen = set()
#         while queue:
#             start = queue.popleft()
#             if start == len(s):
#                 return True
#             for end in range(start + 1, len(s) + 1):
#                 if end in seen:
#                     continue
#                 if s[start:end] in words:
#                     queue.append(end)
#                     seen.add(end)
#         return False


S = "applepenapple"
WordDict = ["apple", "pen"]


print(Solution().wordBreak(S, WordDict))
