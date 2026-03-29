class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimumBuy = float('inf')
        n = len(prices)
        greatest = 0

        for r in range(n):

            minimumBuy = min(minimumBuy, prices[r])

            profit = prices[r] - minimumBuy
            
            greatest = max(greatest, profit)

        return greatest

        # minimumBuy = 1
        #      r
        # [10, 1, 5, 6, 7, 1]