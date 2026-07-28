class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = []
        for i in range (len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                profit.append(prices[i]-min_price)
                continue
        return max(profit)

         