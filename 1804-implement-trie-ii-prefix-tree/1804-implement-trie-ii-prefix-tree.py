class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.wordsEndingHere = 0
        self.wordsStartingHere = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            charIndex = ord(w) - ord('a')
            if not node.links[charIndex]:
                node.links[charIndex] = TrieNode()
            node = node.links[charIndex]
            node.wordsStartingHere += 1
        node.wordsEndingHere += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for w in word:
            charIndex = ord(w) - ord('a')
            if not node.links[charIndex]:
                return 0
            node = node.links[charIndex]
        return node.wordsEndingHere

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for w in prefix:
            charIndex = ord(w) - ord('a')
            if not node.links[charIndex]:
                return 0
            node = node.links[charIndex]
        return node.wordsStartingHere

    def erase(self, word: str) -> None:
        node = self.root
        for w in word:
            charIndex = ord(w) - ord('a')
            node = node.links[charIndex]
            node.wordsStartingHere -= 1
        node.wordsEndingHere -= 1


# Your Trie object will be instantiated and called as such:

trie = Trie()
trie.insert("apple")
trie.insert("apple")
print(trie.countWordsEqualTo("apple"))
print(trie.countWordsStartingWith("app"))
trie.erase("apple")
print(trie.countWordsEqualTo("apple"))
print(trie.countWordsStartingWith("app"))
trie.erase("apple")
print(trie.countWordsStartingWith("app"))
