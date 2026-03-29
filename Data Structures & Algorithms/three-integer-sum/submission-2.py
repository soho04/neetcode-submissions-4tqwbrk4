class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            
            l, r = index + 1, len(nums) - 1
            while l < r:
                sum = value + nums[l] + nums[r]
                if sum == 0 and [value, nums[l], nums[r]] not in res:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1        

        return res




        