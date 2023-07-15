class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.empty())
            return "";
        if (strs.size() == 1)
            return strs[0];
        string ans = "";
        int min_len = 200;

        for (int i = 0; i < strs.size(); i++)
            if (strs[i].size() < min_len)
                min_len = strs[i].size();

        for (int i = 0; i < min_len; i++)
        {
            for (int j = 0; j < strs.size()-1; j++)
            {
                if (strs[j][i] != strs[j + 1][i])
                {
                    return ans;
                }
            }
            ans += strs[0][i];
        }
        return ans;
    }
};