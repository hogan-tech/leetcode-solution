# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.n = 0
        self.words = list()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode

            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return ""
            node = node.children[char]
        return node.words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products:
            trie.insert(word)
        ans, cur = [], ''
        for c in searchWord:
            cur += c
            ans.append(trie.search(cur))
        return ans


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(Solution().suggestedProducts(products, searchWord))
