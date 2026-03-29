class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0 

        nums_set = set(nums)
        greatest_count = 1

        for number in nums_set:
            if number - 1 not in nums_set:
                current_number = number
                count = 1
                
                while current_number + 1 in nums_set:
                    current_number += 1
                    count += 1
                greatest_count = max(count, greatest_count)
                count = 1

        return greatest_count

    # [2, 20, 4, 10, 3, 4, 5]
    # [2, 20, 4, 10, 3, 5]

    # current_number = 5

                

        