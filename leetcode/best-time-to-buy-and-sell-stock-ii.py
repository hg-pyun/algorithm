class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_length = len(prices)

        if prices_length == 0:
            return 0

        min_price = prices[0]
        profit = 0
        profit_sum = 0

        for i in range(prices_length):
            min_price = min(min_price, prices[i])
            profit = max(prices[i] - min_price, profit)

            if i == prices_length - 1:
                profit_sum += profit
                break

            if prices[i] > prices[i + 1]:
                profit_sum += profit
                min_price = sys.maxsize
                profit = 0

        return profit_sum
