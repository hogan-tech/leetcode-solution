# insert()
# time complexity: O(l)
# space complexity: O(l)
# search()
# time complexity: O(l)
# space complexity: O(1)
# search prefix()
# time complexity: O(l)
# space complexity: O(1)
class TrieNode:
    def __init__(self, char: str = ""):
        self.char = char
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                newNode = TrieNode()
                node.children[c] = newNode
                node = newNode
        node.isEnd = True

    def search(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                return False    
            node = node.children[c]
        return node.isEnd
    
    def startsWith(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
