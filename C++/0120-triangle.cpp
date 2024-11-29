class Solution {
 public:
  int minimumTotal(vector<vector<int>>& triangle) {
    for (int row = 1; row < triangle.size(); row++) {
      for (int col = 0; col < triangle[row].size(); col++) {
        int min_sum = INT_MAX;
        if (col > 0) {
          min_sum = triangle[row - 1][col - 1];
        }
        if (col < row) {
          min_sum = min(min_sum, triangle[row - 1][col]);
        }
        int path = min_sum + triangle[row][col];
        triangle[row][col] = path;
      }
    }
    int smallest = INT_MAX;
    int row_amount = triangle.size();
    for (int j = 0; j < triangle[row_amount - 1].size(); j++) {
      smallest = min(triangle[row_amount - 1][j], smallest);
    }
    return smallest;
  }
};