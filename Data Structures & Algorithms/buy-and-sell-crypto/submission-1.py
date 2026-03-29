class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, best = 0, 0 

        while left < len(prices):
            
            sell_price = 0

            for right in range(left, len(prices)):

                sell_price = max(sell_price, prices[right])

            if sell_price:

                best = max(best, sell_price - prices[left])
            
            left += 1

        return best