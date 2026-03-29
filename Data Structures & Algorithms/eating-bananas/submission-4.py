class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        right = max(piles)
        left = 1
        best = float('inf')

        while left <= right:
            speed = (left + right) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile/speed)

            if time <= h:
                best = min(speed, best)
                right = speed-1

            else:
                left = speed + 1
            
        return best

        
