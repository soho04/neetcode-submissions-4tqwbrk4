class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        nums.sort()

        count, greatest = 1, 1

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                count += 1
            else:
                greatest = max(greatest, count) 
                count = 1
            
        greatest = max(greatest, count)    
            

        return greatest if nums else 0

        
        