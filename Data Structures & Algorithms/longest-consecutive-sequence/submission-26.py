class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums_set = set(nums)
        curr_number = None
        greatest = 1

        print(nums_set)

        for number in nums_set:

            if number-1 in nums_set:
                curr_number = number-1
                count = 1
                while curr_number+1 in nums_set:
                    count += 1
                    curr_number += 1
                    greatest = max(greatest, count)

        return greatest
                

        