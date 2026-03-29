class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0: # Starting index is positive, we stray from 0
                break
            
            if i > 0 and a == nums[i-1]: # Starting index is the same again i.e. [-1, -1] which will yield the same combination
                continue

            l, r = i + 1, len(nums)-1 

            while l < r: # Now two pointers

                threesum = a + nums[l] + nums[r]

                if threesum > 0: 
                    r -= 1
                
                elif threesum < 0:
                    l += 1
                
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 
                    r -= 1

                    while nums[l] == nums[l-1] and l < r: # Skip duplicates again
                        l += 1

                    while nums[r] == nums[r+1] and l < r:
                        r -= 1



        return res
        