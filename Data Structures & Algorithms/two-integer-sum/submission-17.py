class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        difference_map = {} # Initialise hash map because it has O(1) time complexity for lookup

        for i in range(len(nums)):
            complement = target - nums[i] # Find complement
            if complement in difference_map:
                return [difference_map[complement], i]
            else:
                difference_map[nums[i]] = i
        


        