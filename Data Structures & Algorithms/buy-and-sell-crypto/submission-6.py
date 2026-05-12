class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, profit = 0, 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            profit = max(profit, prices[r] - prices[l])

        return profit