class Solution {
 public:
  int minCostClimbingStairs(vector<int>& cost) {
    vector<int> min_sum(cost.size() + 1);
    for (int i = 2; i < min_sum.size(); i++) {
      min_sum[i] =
          min(min_sum[i - 1] + cost[i - 1], min_sum[i - 2] + cost[i - 2]);
    }
    return min_sum[min_sum.size() - 1];
  }
};