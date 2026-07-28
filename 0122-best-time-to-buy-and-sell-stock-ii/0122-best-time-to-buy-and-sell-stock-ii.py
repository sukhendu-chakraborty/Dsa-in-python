class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range (len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                profit = profit + (prices[i]-min_price)
                min_price = prices[i]
                continue
        return profit