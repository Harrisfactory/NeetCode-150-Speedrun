class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1

        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            if prices[r] < prices[l]:
                l = r
                r+=1
                continue
            r+=1

        return max_profit