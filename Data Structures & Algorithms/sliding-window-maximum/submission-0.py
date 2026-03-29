class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        arr = []
        l = 0

        for r in range(k, len(nums)+1):
            print(nums[l:r])
            arr.append(max(nums[l:r]))
            l += 1


        return arr