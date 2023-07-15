class Solution {
 public:
  vector<vector<int>> permute(vector<int>& num) {
    vector<vector<int>> res;
    vector<int> out, visited(num.size(), 0);
    permuteDFS(num, 0, visited, out, res);
    return res;
  }
  void permuteDFS(vector<int>& num, int level, vector<int>& visited,
                  vector<int>& out, vector<vector<int>>& res) {
    if (level == num.size()) {
      res.push_back(out);
      return;
    }
    for (int i = 0; i < num.size(); ++i) {
      if (visited[i] == 1) continue;
      visited[i] = 1;
      out.push_back(num[i]);
      permuteDFS(num, level + 1, visited, out, res);
      out.pop_back();
      visited[i] = 0;
    }
  }
};