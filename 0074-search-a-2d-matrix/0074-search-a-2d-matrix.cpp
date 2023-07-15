class Solution {
 public:
  bool searchMatrix(vector<vector<int>> &matrix, int target) {
    int row = matrix.size();
    if (row == 0) return false;
    int col = matrix[0].size();
    int left = 0;
    int right = row * col - 1;
    int pivot, pivot_element;
    while (left <= right) {
      pivot = (left + right) / 2;
      pivot_element = matrix[pivot / col][pivot % col];
      if (target == pivot_element) {
        return true;
      }
      if (target < pivot_element) {
        right = pivot - 1;
      } else {
        left = pivot + 1;
      }
    }
    return false;
  }
};