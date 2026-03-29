class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        res = []

        nums.sort()

        for i, n in enumerate(nums):

            j, k = i + 1, len(nums)-1

            while j < k:

                target = n + nums[j] + nums[k]

                if target == 0 and [n, nums[j], nums[k]] not in res:
                    res.append([n, nums[j], nums[k]])
                    j += 1

                elif target > 0:
                    k -= 1
                
                else:
                    j += 1

        return res

            

            

        