class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int max = -100000;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            sum += nums[i];
            if (sum < nums[i])
            {
                sum = nums[i];
            }
            max = (max > sum ? max : sum);
        }
        return max;
    }
};