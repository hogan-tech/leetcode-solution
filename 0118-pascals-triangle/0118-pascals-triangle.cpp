class Solution
{
public:
    vector<vector<int> > generate(int numRows)
    {
        vector<vector<int> > ret;
        ret.reserve(numRows);
        for (int n = 0; n < numRows; n++)
        {
            vector<int> row;
            row.push_back(1); 
            row.reserve(n + 1);
            for (int k = 1; k <= n; k++)
            {
                row.push_back(row.back() * (n + 1 - k) / k);
            }
            ret.push_back(row);
        }
        return ret;
    }
};