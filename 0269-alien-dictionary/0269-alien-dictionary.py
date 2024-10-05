# time complexity: O(C)
# space complexity: O(1)
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


words = ["wrt", "wrf", "er", "ett", "rftt"]
print(Solution().alienOrder(words))
