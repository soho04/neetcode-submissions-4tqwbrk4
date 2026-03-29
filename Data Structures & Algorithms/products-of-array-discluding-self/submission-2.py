class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        i, j = 0, 0
        arr = []
        acc = 1

        while i < len(nums):
            while j < len(nums):
                if i == j:
                    j += 1
                else:
                    acc *= nums[j]
                    j += 1
            j = 0
            arr.append(acc)
            acc = 1
            i += 1
        
        return arr
            

