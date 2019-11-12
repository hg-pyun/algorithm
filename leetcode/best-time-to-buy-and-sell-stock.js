/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min = prices[0];
    let profit = 0;
    
    for(let i = 0; i < prices.length; i++) {
        min = Math.min(prices[i], min);
        profit = Math.max(prices[i] - min, profit);
    }
    
    return profit;
};
