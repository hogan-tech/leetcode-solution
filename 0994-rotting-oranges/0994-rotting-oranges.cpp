class Solution {
 public:
  int orangesRotting(vector<vector<int>>& grid) {
    queue<pair<int, int>> q;
    int freshOrange = 0;
    int rows = grid.size();
    int cols = grid[0].size();

    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (grid[r][c] == 2) {
          q.push({r, c});
        } else {
          if (grid[r][c] == 1) {
            freshOrange++;
          }
        }
      }
    }

    q.push({-1, -1});

    int minutesElapsed = -1;
    int dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    while (!q.empty()) {
      pair<int, int> curr = q.front();
      q.pop();
      int cur_row = curr.first;
      int cur_col = curr.second;

      if (cur_row == -1) {
        minutesElapsed++;
        if (!q.empty()) {
          q.push({-1, -1});
        }
      } else {
        for (int i = 0; i < 4; i++) {
          int new_row = cur_row + dir[i][0];
          int new_col = cur_col + dir[i][1];
          if (new_row >= 0 && new_col >= 0 && new_row < rows &&
              new_col < cols) {
            if (grid[new_row][new_col] == 1) {
              grid[new_row][new_col] = 2;
              freshOrange--;
              q.push({new_row, new_col});
            }
          }
        }
      }
    }
    return (freshOrange == 0 ? minutesElapsed : -1);
  }
};