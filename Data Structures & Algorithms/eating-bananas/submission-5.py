class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)

        while left < right:

            eatingSpeed = (left + right) // 2
            eatingTime = 0

            for pile in piles:

                eatingTime += math.ceil(pile / eatingSpeed)

            print(eatingSpeed)

            if eatingTime <= h:
                right = eatingSpeed

            else:
                left = eatingSpeed + 1
                print("left is now ", left)

        return left
        

        # [1, 4, 3, 2]
        #  l  r     
        # [1, 2, 3, 4] eating speeds
        # at speed 1, it takes 10
        # at speed 2, it takes 6
        # at speed 3, it takes 5

