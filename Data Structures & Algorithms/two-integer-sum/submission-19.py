class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sums = defaultdict(int)

        for index, number in enumerate(nums):

            difference = target - number

            if difference in sums.keys():
                return [sums[difference], index]

            sums[number] = index

        #