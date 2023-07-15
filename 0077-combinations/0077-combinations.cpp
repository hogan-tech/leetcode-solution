class Solution {
  vector<vector<int>> ans;
  // n = 4;k = 2;
  int N, K;
  void findCombination(int start, vector<int> &row) {
    if (row.size() == K) {
      ans.push_back(row);
      return;
    }

    if (N - start + 1 + row.size() >= K) {
      for (int i = start; i <= N; i++) {
        row.push_back(i);
        findCombination(i + 1, row);
        row.pop_back();
      }
    }
  }

 public:
  vector<vector<int>> combine(int n, int k) {
    vector<int> row = vector<int>();
    N = n;
    K = k;
    findCombination(1, row);
    return ans;
  }
};