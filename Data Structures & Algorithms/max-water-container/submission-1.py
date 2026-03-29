class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        greatest = 0

        for i in range(len(heights)):
            
            r = len(heights)-1

            while i < r:
            
                height = min(heights[i], heights[r])
                length = r - i
                area = height * length
                print(height, " * ", length, " = ", area)
                
                greatest = max(greatest, area)
                r -= 1



        return greatest