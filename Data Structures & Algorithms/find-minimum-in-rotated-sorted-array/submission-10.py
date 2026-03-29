class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1
        minimum = 99

        if nums[left] < nums[right]:
            return nums[left]


        while left <= right:
            
            middle = (left + right) // 2

            minimum = min(nums[middle], minimum)
            
            if nums[right] < nums[middle]:
                left = middle + 1

            else:
                right = middle - 1

        return minimum