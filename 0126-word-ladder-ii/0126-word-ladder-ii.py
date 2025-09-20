# time complexity: O(n*k^2 + a)
# space complexity: O(n*k)
from collections import deque
from typing import Deque, Dict, List, Set


class Solution:
    def __init__(self):
        self.adjList: Dict[str, List[str]] = {}
        self.currPath: List[str] = []
        self.shortestPaths: List[List[str]] = []

    def findNeighbors(self, word: str, wordSet: Set[str]) -> List[str]:
        neighbors: List[str] = []
        charList = list(word)
        for i in range(len(charList)):
            oldChar = charList[i]
            for c in "abcdefghijklmnopqrstuvwxyz":
                charList[i] = c
                newWord = "".join(charList)
                if c == oldChar or newWord not in wordSet:
                    continue
                neighbors.append(newWord)
            charList[i] = oldChar
        return neighbors

    def backtrack(self, source: str, destination: str):
        if source == destination:
            tempPath = self.currPath.copy()
            tempPath.reverse()
            self.shortestPaths.append(tempPath)

        if source not in self.adjList:
            return

        for neighbor in self.adjList[source]:
            self.currPath.append(neighbor)
            self.backtrack(neighbor, destination)
            self.currPath.pop()

    def bfs(self, beginWord: str, endWord: str, wordSet: Set[str]):
        q: Deque[str] = deque([beginWord])
        wordSet.discard(beginWord)
        isEnqueued: Dict[str, bool] = {beginWord: True}
        while q:
            visited: List[str] = []
            for _ in range(len(q)):
                currWord = q.popleft()
                neighbors = self.findNeighbors(currWord, wordSet)
                for neighbor in neighbors:
                    visited.append(neighbor)
                    if neighbor not in self.adjList:
                        self.adjList[neighbor] = []
                    self.adjList[neighbor].append(currWord)
                    if neighbor not in isEnqueued:
                        q.append(neighbor)
                        isEnqueued[neighbor] = True
            for word in visited:
                wordSet.discard(word)

    def findLadders(
            self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet: Set[str] = set(wordList)
        self.bfs(beginWord, endWord, wordSet)
        self.currPath = [endWord]
        self.backtrack(endWord, beginWord)

        return self.shortestPaths


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().findLadders(beginWord, endWord, wordList))
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(Solution().findLadders(beginWord, endWord, wordList))
