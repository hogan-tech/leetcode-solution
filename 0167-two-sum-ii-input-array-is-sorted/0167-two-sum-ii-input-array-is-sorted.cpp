class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> twoSum;
        int low = 0;
        int high = nums.size() - 1;
        while (low < high)
        {
            int sum = nums[low] + nums[high];
            if (sum == target)
            {
                twoSum.push_back(low + 1);
                twoSum.push_back(high + 1);
                return twoSum;
            }
            if (sum > target)
                --high;
            if (sum < target)
                ++low;
        }
        twoSum.push_back(-1);
        twoSum.push_back(-1);
        return twoSum;
    }
};