class Solution {
  int findPath(vector<vector<int>>& grid, int x, int y) {
    int counter = 0;
    if (grid[x][y] == 1) {
      counter++;
      grid[x][y] = 0;
      if (grid[x + 1][y] == 1) {
        counter += findPath(grid, x + 1, y);
      }
      if (grid[x - 1][y] == 1) {
        counter += findPath(grid, x - 1, y);
      }
      if (grid[x][y + 1] == 1) {
        counter += findPath(grid, x, y + 1);
      }
      if (grid[x][y - 1] == 1) {
        counter += findPath(grid, x, y - 1);
      }
    }
    return counter;
  }

 public:
  int maxAreaOfIsland(vector<vector<int>>& grid) {
    int sum = 0;
    vector<vector<int>> big_grid(grid.size() + 2,
                                 vector<int>(grid[0].size() + 2, 0));
    for (int i = 0; i < grid.size(); i++) {
      for (int j = 0; j < grid[0].size(); j++) {
        big_grid[i + 1][j + 1] = grid[i][j];
      }
    }
    for (int i = 0; i < big_grid.size(); i++) {
      for (int j = 0; j < big_grid[0].size(); j++) {
        sum = max(findPath(big_grid, i, j), sum);
      }
    }
    return sum;
  }
};