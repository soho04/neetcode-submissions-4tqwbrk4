class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        greatest = 0

        i, j = 0, len(heights)-1

        while i < j:

            area = (j - i) * min(heights[i], heights[j])

            greatest = max(greatest, area)

            if heights[i] > heights[j]:
                j -= 1
            
            else:
                i += 1

        return greatest
