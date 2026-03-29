class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        placeholder1 = 0
        placeholder2 = 0

        for i in range(len(nums)):

            indexMark = abs(nums[i])-1
            print(nums)

            if nums[indexMark] > 0:
                nums[indexMark] = -nums[indexMark]
            
            else:
                return abs(nums[i])
