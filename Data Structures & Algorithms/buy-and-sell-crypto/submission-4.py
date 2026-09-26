class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l = 0
        r = 0
        while r < len(prices):
            profit = 0
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
            else:
                l = r
            max_profit = max(max_profit,profit)
            r += 1
        return max_profit
