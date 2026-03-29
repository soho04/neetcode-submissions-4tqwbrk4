class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums.sort()
        run, greatest = 1, 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i-1] + 1:
                run += 1
                greatest = max(run, greatest)

            elif nums[i] == nums[i-1]:
                continue

            else:
                run = 1

        return greatest
        