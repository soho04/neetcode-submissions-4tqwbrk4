class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []

        result = []
        nums.sort()

        i = 0

        print(nums)

        while i < len(nums):

            left, right = i + 1, len(nums)-1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    print(i, left, right)
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < len(nums)-1 and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while right+1 < len(nums)-1 and right>0 and nums[right] == nums[right+1]:
                        right -= 1
                    
                elif total < 0:
                    left += 1
                    while left < len(nums)-1 and nums[left] == nums[left-1]:
                        left += 1
                
                else:
                    right -= 1
                    while right+1 < len(nums)-1 and right>0 and nums[right] == nums[right+1]:
                        right -= 1

            while ((i + 1) < len(nums)-1) and nums[i+1] == nums[i]:
                i += 1
            i += 1
            

        return result

        #  i   l           r
        # -4, -1, -1, 0, 1, 2

                