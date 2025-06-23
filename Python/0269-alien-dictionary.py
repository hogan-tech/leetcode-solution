# time complexity: O(C)
# space complexity: O(1)
from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        reverseAdjList = {c: [] for word in words for c in word}
        for firstWord, secondWord in zip(words, words[1:]):
            for c, d in zip(firstWord, secondWord):
                if c != d:
                    reverseAdjList[d].append(c)
                    break
            else:
                if len(secondWord) < len(firstWord):
                    return ""
        seen = {}
        output = []

        def visit(node):
            if node in seen:
                return seen[node]
            seen[node] = False
            for nextNode in reverseAdjList[node]:
                result = visit(nextNode)
                if not result:
                    return False
            seen[node] = True
            output.append(node)
            return True

        if not all(visit(node) for node in reverseAdjList):
            return ""
        return "".join(output)

# time complexity: O(C)
# space complexity: O(1)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = defaultdict(set)
        indegree = defaultdict(int)
        
        for word in words:
            for c in word:
                indegree[c] = 0

        for word1, word2 in zip(words, words[1:]):
            foundDiff = False
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in adjList[c1]:
                        adjList[c1].add(c2)
                        indegree[c2] += 1
                    foundDiff = True
                    break
            if not foundDiff and len(word2) < len(word1):
                return ""

        result = []
        queue = deque()
        for currC in indegree:
            if indegree[currC] == 0:
                queue.append(currC)
                
        while queue:
            currC = queue.popleft()
            result.append(currC)
            for nextC in adjList[currC]:
                indegree[nextC] -= 1
                if indegree[nextC] == 0:
                    queue.append(nextC)

        if len(result) < len(indegree):
            return ""
        return "".join(result)


words = ["wrt", "wrf", "er", "ett", "rftt"]
print(Solution().alienOrder(words))
words = ["z", "x"]
print(Solution().alienOrder(words))
words = ["z", "x", "z"]
print(Solution().alienOrder(words))
words = ["mzosr", "mqov", "xxsvq", "xazv", "xazau", "xaqu",
         "suvzu", "suvxq", "suam", "suax", "rom", "rwx", "rwv"]
print(Solution().alienOrder(words))
