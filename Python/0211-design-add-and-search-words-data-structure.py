# time complexity: O(M)
# space complexity: O(M)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.maxLen = 0

    def addWord(self, word: str) -> None:
        node = self.root
        l = 0
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            l += 1
        self.maxLen = max(self.maxLen, l)
        node.isEnd = True

    def search(self, word: str) -> bool:
        if len(word) > self.maxLen:
            return False

        def helper(idx, node):
            for i in range(idx, len(word)):
                if word[i] == ".":
                    for child in node.children.values():
                        if helper(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.isEnd
        return helper(0, self.root)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))
