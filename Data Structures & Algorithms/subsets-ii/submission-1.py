class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtrack(i, subset):

            if i >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i+1, subset)

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            subset.pop()
            backtrack(i+1, subset)

        backtrack(0, [])

        return res


        # 1, 1, 2

        # backtrack(0, ()) curr = [1, ]
        # backtrack(1, ()) curr = [1, ] -> backtrack(2, ())
        # backtrack(2, ()) curr = [1, 1, 2] res = [1, 1, 2]
        #

            