class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        count = 1
        i = 0
        greatest = 1

        print(nums)

        if not nums:
            return 0

        while i < len(nums):

            if i != 0 and nums[i] == nums[i-1] + 1:
                print("got a sequence ", nums[i], nums[i-1])
                count += 1

            elif nums[i] == nums[i-1]:
                i += 1
                continue

            else:
                count = 1

            greatest = max(count, greatest)

            i += 1

        return greatest


        

        