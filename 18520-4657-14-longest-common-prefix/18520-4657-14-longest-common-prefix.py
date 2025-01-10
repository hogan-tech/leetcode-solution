# time complexity: O(s+m)
# space complexity: O(s)
from typing import List


class TrieNode:
    def __init__(self, char=""):
        self.children = {}
        self.char = char
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        def findLongestCommonPrefix(trie: Trie):
            prefix = ""
            node = trie.root
            while node and not node.isEnd and len(node.children) == 1:
                char, childNode = list(node.children.items())[0]
                prefix += char
                node = childNode
            return prefix

        return findLongestCommonPrefix(trie)


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
strs = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(strs))
