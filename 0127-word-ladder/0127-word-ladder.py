from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque([beginWord])
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                current = list(queue.popleft())
                for j in range(len(current)):
                    tmp = current[j]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        current[j] = c
                        nextWord = "".join(current)
                        if nextWord in wordSet:
                            if nextWord == endWord:
                                return count + 1
                            queue.append(nextWord)
                            wordSet.remove(nextWord)
                    current[j] = tmp
            count += 1
        return 0
