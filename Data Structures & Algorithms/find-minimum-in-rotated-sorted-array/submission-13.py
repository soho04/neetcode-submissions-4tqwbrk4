class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1

        while left < right:

            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1

            else:
                right = middle

        return nums[left]




        #      m
        # [0,1,2,3,4,5]
        # [5,0,1,2,3,4]
        # [4,5,0,1,2,3]
        # [3,4,5,0,1,2]
        # [2,3,4,5,0,1]

        # We can observe that if the middle is greater than the value at the right pointer,
        # We have just traversed a high point, and as a result, reset to the minimum value,
        # To increment through again
        # E.g. 5 > 2, so we must have reset to 0 at some point in the right hand side
        # Else, 1 < 4, we have not reset, and the minimum is to the left
        