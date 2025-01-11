# time complexity: O(n)
# space complexity: O(n)
class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = -1
        if player == 1:
            currentPlayer = 1
        n = len(self.rows)
        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer
        if row == col:
            self.diagonal += currentPlayer
        if col == (n - row - 1):
            self.antiDiagonal += currentPlayer

        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.antiDiagonal) == n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
print(obj.move(0, 0, 1))
print(obj.move(0, 2, 2))
print(obj.move(2, 2, 1))
print(obj.move(1, 1, 2))
print(obj.move(2, 0, 1))
print(obj.move(1, 0, 2))
print(obj.move(2, 1, 1))
