class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        candidates.sort()


        def backtrack(total, start):

            if total == target:
                res.append(curr[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                curr.append(candidates[i])
                backtrack(total+candidates[i], i+1)
                curr.pop()

        backtrack(0, 0)

        return res





