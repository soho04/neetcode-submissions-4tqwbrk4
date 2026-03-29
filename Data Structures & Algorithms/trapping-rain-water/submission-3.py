class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l, r = 0, len(height)-1
        LMax, RMax = height[l], height[r]
        res = 0

        while l < r:
            
            if height[l] <= height[r]:

                l += 1
                if LMax - height[l] > 0:
                    res += LMax - height[l]
                    print("res is now ", res, " after adding from the left ")
                LMax = max(height[l], LMax)

            else:

                r -= 1
                if RMax - height[r] > 0:
                    res += RMax - height[r]
                    print("res is now ", res, " after adding from the right ")
                RMax = max(height[r], RMax)

        return res
                



