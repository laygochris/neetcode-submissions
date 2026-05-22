class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        mProfit = 0

        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1

            profit = prices[r] - prices[l]
            mProfit = max(mProfit, profit)
        
        return mProfit