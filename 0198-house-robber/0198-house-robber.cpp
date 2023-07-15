class Solution {
 public:
  int rob(vector<int>& nums) {
    int total = nums.size();
    if (total == 0) return 0;
    vector<int> maxRobbedAmount(total + 1, 0);
    maxRobbedAmount[total] = 0;
    maxRobbedAmount[total - 1] = nums[total - 1];
    for (int i = total - 2; i >= 0; i--) {
      maxRobbedAmount[i] =
          max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i]);
    }
    return maxRobbedAmount[0];
  }
};