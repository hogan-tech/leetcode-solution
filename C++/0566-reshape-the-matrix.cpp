class Solution
{
public:
    vector<vector<int> > matrixReshape(vector<vector<int> > &nums, int r, int c)
    {
        vector<vector<int> > newMatrix(r, vector<int>(c, 0));
        int originalRaw = nums.size();
        int originalColumn = nums[0].size();
        if (originalRaw * originalColumn != r * c)
            return nums;

        int newRaw = 0, newColumn = 0;
        for (int i = 0; i < originalRaw; i++)
        {
            for (int j = 0; j < originalColumn; j++)
            {
                newMatrix[newRaw][newColumn] = nums[i][j];
                newColumn++;
                if (newColumn == c)
                {
                    newColumn = 0;
                    newRaw++;
                }
            }
        }
        return newMatrix;
    }
};