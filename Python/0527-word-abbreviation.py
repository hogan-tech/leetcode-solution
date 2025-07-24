# time complexity: O(n*l)
# space complexity: O(n*l)
from typing import List


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            cands = [word[0] + word[-1]] + list(word[1:-1])
            for i, w in enumerate(cands):
                node = node.setdefault(w, {})
                rest = len(cands) - i - 1
                node[rest] = node.get(rest, 0) + 1

        result = []
        for word in words:
            if len(word) <= 3:
                result.append(word)
                continue
            node = trie
            cands = [word[0] + word[-1]] + list(word[1:-1])
            for i, w in enumerate(cands):
                node = node[w]
                rest = len(cands) - i - 1
                if rest > 1 and node[rest] < 2:
                    result.append(word[:i+1]+str(rest)+word[-1])
                    break
                elif rest <= 1:
                    result.append(word)
                    break

        return result


words = ["like", "god", "internal", "me", "internet",
         "interval", "intension", "face", "intrusion"]
print(Solution().wordsAbbreviation(words))
words = ["aa", "aaa"]
print(Solution().wordsAbbreviation(words))
