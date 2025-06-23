# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque()
        queue.append(beginWord)
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                currWord = queue.popleft()
                if currWord == endWord:
                    return count
                for wordIdx in range(len(currWord)):
                    for nextC in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = currWord[:wordIdx] + nextC + currWord[wordIdx + 1:]
                        if nextWord in wordSet:
                            queue.append(nextWord)
                            wordSet.remove(nextWord)
            count += 1
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(Solution().ladderLength(beginWord, endWord, wordList))
