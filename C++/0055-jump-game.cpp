class Solution {
 public:
  bool canJump(vector<int>& nums) { 
      int last_pos = nums.size()-1;
      for(int i = nums.size()-1;i >=0;i --){
          if(nums[i] + i >= last_pos){
              last_pos = i;
          }
      }
      return last_pos == 0; 
    }
};