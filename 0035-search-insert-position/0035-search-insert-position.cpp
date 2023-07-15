class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int index = 0;
        if (nums.size() == 1)
            return (nums[0] < target ? 1 : 0);
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == target)
                return i;
            if (nums[i] < target && nums[i + 1] > target)
                return i + 1;
            if (nums[nums.size() - 1] < target)
                return nums.size();
        }
        return index;
    }
};