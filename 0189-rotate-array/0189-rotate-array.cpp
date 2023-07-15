class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        vector<int> a = nums;
        for (int i = 0; i < nums.size(); i++)
        {
            a[(k + i) % nums.size()] = nums[i];
        }
        for (int i = 0; i < nums.size(); i++)
        {
            nums[i] = a[i];
        }
    }
};