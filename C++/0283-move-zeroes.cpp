class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        vector<int> output;
        output.reserve(nums.size());
        int count = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
                count++;
            if (nums[i])
                output.push_back(nums[i]);
        }
        for (int i = 0; i < count; i++)
            output.push_back(0);
        nums = output;
    }
};