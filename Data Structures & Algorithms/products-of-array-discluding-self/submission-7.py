class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] + nums[:] + [1]
        postfix = [1] + nums[:] + [1]
        
        product = 1

        for i in range(1, len(prefix)):
            product *= prefix[i]
            prefix[i] = product

        product = 1

        for j in range(len(postfix)-1, -1, -1):
            product *= postfix[j]
            postfix[j] = product

        print(prefix, postfix)

        for index in range(len(nums)):
            nums[index] = prefix[index] * postfix[index+2]

        # 1,  1,  2,  8,  48, 48
        #     1,  2,  4,  6
        # 48, 48, 48, 24, 6,  1



        return nums

        