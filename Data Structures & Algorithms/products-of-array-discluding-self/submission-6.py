class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        runner = 1
        for i in range(len(nums)):
            res[i] = runner
            runner *= nums[i]

        runner = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= runner
            runner *= nums[i]

        return res

