class Solution {
  void twoSumII(vector<int>& nums, int i, vector<vector<int>>& res) {
    int lo = i + 1, hi = nums.size() - 1;
    while (lo < hi) {
      int sum = nums[i] + nums[lo] + nums[hi];
      if (sum < 0) {
        ++lo;
      } else if (sum > 0) {
        --hi;
      } else {
        res.push_back({nums[i], nums[lo++], nums[hi--]});
        while (lo < hi && nums[lo] == nums[lo - 1]) ++lo;
      }
    }
  }

 public:
  vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> output;
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size() && nums[i] <= 0; i++) {
      if (i == 0 || nums[i - 1] != nums[i]) {
          twoSumII(nums, i, output);
      }
    }
    return output;
  }
};