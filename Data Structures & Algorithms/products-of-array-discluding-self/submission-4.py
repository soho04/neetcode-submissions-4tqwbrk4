class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * (len(nums) + 2)
        postfix = [1] * (len(nums) + 2)

        running = 1
        for i in range(len(nums)):
            prefix[i+1] = running * nums[i]
            running *= nums[i]

        running = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i+1] = running * nums[i]
            running *= nums[i]

        for i in range(len(nums)):
            nums[i] = prefix[i] * postfix[i+2]

        return nums