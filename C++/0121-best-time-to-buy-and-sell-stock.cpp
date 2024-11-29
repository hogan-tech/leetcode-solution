class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int min = 10000;
        int max_profit = 0;
        for (int i = 0; i < prices.size(); i++)
        {
            if (min > prices[i])
            {
                min = prices[i];
            }
            else
            {
                max_profit = max(max_profit, prices[i] - min);
            }
        }
        return max_profit;
    }
};