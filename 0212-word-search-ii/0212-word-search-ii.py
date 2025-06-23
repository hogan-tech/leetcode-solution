# time complexity: O(M(4*3^(L-1)))
# space complexity: O(n)
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORDKEY = "$"
        trie = {}

        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORDKEY] = word

        ROW = len(board)
        COL = len(board[0])
        matchedWords = []

        def backtracking(currR: int, currC: int, parent: dict):
            letter = board[currR][currC]
            currNode = parent[letter]
            wordMatch = currNode.pop(WORDKEY, False)
            if wordMatch:
                matchedWords.append(wordMatch)
            board[currR][currC] = "#"
            for dR, dC in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and board[nextR][nextC] in currNode:
                    backtracking(nextR, nextC, currNode)

            board[currR][currC] = letter

            if not currNode:
                parent.pop(letter)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] in trie:
                    backtracking(r, c, trie)

        return matchedWords

# time complexity: O(m*l + n*4^l)
# space complexity: O(m*l + n)
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
            node = node.children.get(c)
        node.isEnd = True

    def startWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def removeChar(self, word):
        node = self.root
        childList = []

        for c in word:
            childList.append([node, c])
            node = node.children[c]

        for parent, childChar in childList[::-1]:
            target = parent.children[childChar]
            if target.children:
                return
            del parent.children[childChar]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        ROW = len(board)
        COL = len(board[0])
        for word in words:
            trie.insert(word)

        def backtrack(node: TrieNode, r: int, c: int, word=""):
            if node.isEnd:
                result.append(word)
                node.isEnd = False
                trie.removeChar(word)

            if 0 <= r < ROW and 0 <= c < COL:
                currC = board[r][c]
                child = node.children.get(currC)
                if child is not None:
                    word += currC
                    board[r][c] = None
                    for dR, dC in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nextR = r + dR
                        nextC = c + dC
                        backtrack(child, nextR, nextC, word)
                    board[r][c] = currC

        result = []
        for r in range(ROW):
            for c in range(COL):
                backtrack(trie.root, r, c)

        return result


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
print(Solution().findWords(board, words))
board = [["a", "b"], ["c", "d"]]
words = ["abcb"]
print(Solution().findWords(board, words))
