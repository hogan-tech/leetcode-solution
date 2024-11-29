class Solution {
  bool checkRow(vector<vector<char>> &board, int row) {
    unordered_set<char> set;
    for (int i = 0; i < 9; ++i) {
      if (board[row][i] != '.') {
        if (set.count(board[row][i])) {
          return false;
        }
        set.insert(board[row][i]);
      }
    }
    return true;
  }
  bool checkCol(vector<vector<char>> &board, int col) {
    unordered_set<char> set;
    for (int i = 0; i < 9; ++i) {
      if (board[i][col] != '.') {
        if (set.count(board[i][col])) {
          return false;
        }
        set.insert(board[i][col]);
      }
    }
    return true;
  }
  bool checkBox(vector<vector<char>> &board, int row, int col) {
    unordered_set<char> set;
    for (int i = row; i < row + 3; ++i) {
      for (int j = col; j < col + 3; ++j) {
        if (board[i][j] != '.') {
          if (set.count(board[i][j])) {
            return false;
          }
          set.insert(board[i][j]);
        }
      }
    }
    return true;
  }

 public:
  bool isValidSudoku(vector<vector<char>> &board) {
    bool output = true;
    for (int i = 0; i < 9; i++) {
      output = checkRow(board, i);
      if (!output) {
        return output;
      }
    }
    for (int i = 0; i < 9; i++) {
      output = checkCol(board, i);
      if (!output) {
        return output;
      }
    }
    for (int i = 0; i < 9; i += 3) {
      for (int j = 0; j < 9; j += 3) {
        output = checkBox(board, i, j);
        if (!output) {
          return output;
        }
      }
    }
    return true;
  }
};