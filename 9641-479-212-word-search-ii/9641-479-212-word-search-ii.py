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
        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]
            wordMatch = currNode.pop(WORDKEY, False)
            if wordMatch:
                matchedWords.append(wordMatch)
            board[row][col] = "#"
            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if (
                    newRow < 0
                    or newRow >= rowNum
                    or newCol < 0
                    or newCol >= colNum
                ):
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            board[row][col] = letter

            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords

# time complexity: O(n*3^l)
# space complexity: O(m)
class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
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

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def removeChars(self, word):
        node = self.root
        childList = []

        for c in word:
            childList.append([node, c])
            node = node.children[c]

        for parent, childChar in reversed(childList):
            target = parent.children[childChar]
            if target.children:
                return
            del parent.children[childChar]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(trieForWords: Trie, node: TrieNode, grid: List[List[str]], row: int, col: int, result: List[str], word=""):
            if node.isEnd:
                result.append(word)
                node.isEnd = False
                trieForWords.removeChars(word)

            if 0 <= row < ROW and 0 <= col < COL:
                char = grid[row][col]
                child = node.children.get(char)
                if child is not None:
                    word += char
                    grid[row][col] = None
                    for dR, dC in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        dfs(trieForWords, child, grid,
                            row + dR, col + dC, result, word)
                    grid[row][col] = char

        ROW = len(board)
        COL = len(board[0])
        trieForWords = Trie()
        result = []
        for word in words:
            trieForWords.insert(word)

        for r in range(ROW):
            for c in range(COL):
                dfs(trieForWords, trieForWords.root, board, r, c, result)

        return result


board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

print(Solution().findWords(board, words))
