class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # max_profit = 0
        # left = 0 
        # right = 1
        # while right < len(prices):
        #     if prices[right] > prices[left]:

        #         profit = prices[right]-prices[left]
        #         max_profit = max(profit,max_profit)
        #     else:
        #         left = right
        #     right +=1
            
        # return max_profit


        output = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                output = max(output,profit)
            else:
                l = r
            r += 1
        return output
        