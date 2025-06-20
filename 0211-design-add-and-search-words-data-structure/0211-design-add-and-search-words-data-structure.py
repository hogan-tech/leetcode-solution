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
        currLen = 0
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            currLen += 1
        self.maxLen = max(self.maxLen, currLen)
        
        node.isEnd = True

    def search(self, word: str) -> bool:
        if len(word) > self.maxLen:
            return False
        
        def dfs(idx, node):
            for i in range(idx, len(word)):
                if word[i] == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.isEnd
        return dfs(0, self.root)
            



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)