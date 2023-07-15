class Solution {
 public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> list;
    int rows = matrix.size();
    int cols = matrix[0].size();
    int top = 0;
    int bottom = rows - 1;
    int left = 0;
    int right = cols - 1;
    while (list.size() < rows * cols) {
      for (int i = left; i <= right; i++) {
        list.push_back(matrix[top][i]);
      }
      for (int i = top + 1; i <= bottom; i++) {
        list.push_back(matrix[i][right]);
      }
      if (top != bottom) {
        for (int i = right - 1; i >= left; i--) {
          list.push_back(matrix[bottom][i]);
        }
      }
      if (left != right) {
        for (int i = bottom - 1; i > top; i--) {
          list.push_back(matrix[i][left]);
        }
      }
      left++;
      top++;
      right--;
      bottom--;
    }

    return list;
  }
};