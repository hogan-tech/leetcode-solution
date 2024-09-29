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


board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

print(Solution().findWords(board, words))
