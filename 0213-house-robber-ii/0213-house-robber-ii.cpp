class Solution {
  int rob_simple(vector<int>& nums, int start, int end) {
    int t1 = 0;
    int t2 = 0;
    for (int i = start; i <= end; i++) {
      int current = nums[i];
      int temp = t1;
      t1 = max(current + t2, t1);
      t2 = temp;
    }
    return t1;
  }

 public:
  int rob(vector<int>& nums) {
    int total = nums.size();
    if (total == 0) return 0;
    if (total == 1) return nums[0];
    if (total == 2) return max(nums[0], nums[1]);
    int max1 = rob_simple(nums, 0, nums.size() - 2);
    int max2 = rob_simple(nums, 1, nums.size() - 1);
    return max(max1, max2);
  }
};