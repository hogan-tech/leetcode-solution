# time complexity: O(n*l)
# space complexity: O(n*l)
from typing import List


class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isEndOfWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def hasAllPrefixes(self, word):
        node = self.root
        for char in word:
            if (char not in node.children or not node.children[char].isEndOfWord):
                return False
            node = node.children[char]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        longestValidWord = ""

        for word in words:
            trie.insert(word)

        for word in words:
            if trie.hasAllPrefixes(word):
                if len(word) > len(longestValidWord) or (
                    len(word) == len(longestValidWord)
                    and word < longestValidWord
                ):
                    longestValidWord = word

        return longestValidWord


words = ["abc", "bc", "ab", "qwe"]
print(Solution().longestWord(words))
