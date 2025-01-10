# time complexity: O(d*w + s*w^2)
# space complexity: O(d*w + s*w)
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictSet = set(dictionary)
        result = []
        for word in sentence.split(" "):
            for wordIdx in range(len(word)+1):
                if word[:wordIdx] in dictSet:
                    result.append(word[:wordIdx])
                    break
                if wordIdx == len(word):
                    result.append(word[:wordIdx])
        return " ".join(result)

# time complexity: O(n + m)
# space complexity: O(m)
class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def replace(self, word: str):
        node = self.root
        for i, c in enumerate(word):
            if c not in node.children:
                return word

            node = node.children[c]
            if node.isEnd:
                return word[:i + 1]
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for prefix in dictionary:
            trie.insert(prefix)
        newList = sentence.split()
        for i in range(len(newList)):
            newList[i] = trie.replace(newList[i])
        return " ".join(newList)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dictionary, sentence))
