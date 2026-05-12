class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

        return maxProfit
            


        