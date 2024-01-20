/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    profit = 0;
    smallestProfit = 99999;
    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < smallestProfit) {
            smallestProfit = prices[i];
        } else {
            profit = Math.max(profit, prices[i] - smallestProfit);
        }
    }
    return profit;
};

PriceList = [7, 1, 5, 3, 6, 4];

console.log(maxProfit(PriceList));
