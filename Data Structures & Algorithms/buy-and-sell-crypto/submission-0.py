class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, best = 0, 0 

        while left < len(prices):
            
            for right in range(left, len(prices)):

                total = prices[right] - prices[left]

                best = max(best, total)
            
            left += 1

        return best