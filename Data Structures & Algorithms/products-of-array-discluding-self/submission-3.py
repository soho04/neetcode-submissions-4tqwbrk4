class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):
            
            runner = 1
            
            for x in range(len(nums)):
                if i == x:
                    print("i is equal to x", i, x)
                    continue
                else:
                    runner *= nums[x]
                    print("runner is now at ", runner, " after multiplying by ", x)

            res.append(runner)

        return res
