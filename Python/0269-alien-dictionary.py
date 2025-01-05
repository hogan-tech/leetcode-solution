# time complexity: O(C)
# space complexity: O(1)
from collections import Counter, defaultdict, deque
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


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = defaultdict(set)
        counts = Counter({c: 0 for word in words for c in word})

        for word1, word2 in zip(words, words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in adjList[c1]:
                        adjList[c1].add(c2)
                        counts[c2] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""

        result = []
        sourceQueue = deque([c for c in counts if counts[c] == 0])
        while sourceQueue:
            c = sourceQueue.popleft()
            result.append(c)
            for d in adjList[c]:
                counts[d] -= 1
                if counts[d] == 0:
                    sourceQueue.append(d)

        if len(result) < len(counts):
            return ""
        return "".join(result)


words = ["mzosr", "mqov", "xxsvq", "xazv", "xazau", "xaqu",
         "suvzu", "suvxq", "suam", "suax", "rom", "rwx", "rwv"]
print(Solution().alienOrder(words))
