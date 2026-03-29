class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count = 1
        greatest = 1

        nums.sort()
        print(nums)

        if not nums:
            return 0

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1 
                greatest = max(count, greatest)
            else:
                count = 1  
        
        return greatest

        