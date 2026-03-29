class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        permutation = []

        def backtrack(num_set):

            if len(permutation) >= len(nums):
                res.append(permutation[:])
                return

            for n in range(len(nums)):
                if nums[n] not in num_set:
                    num_set.add(nums[n])
                    permutation.append(nums[n])

                    backtrack(num_set)

                    num_set.remove(nums[n])
                    permutation.pop()
                else:
                    continue

        backtrack(set())

        return res