class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_set = set()

        for number in nums:

            if number in nums_set:
                return True

            nums_set.add(number)

        return False