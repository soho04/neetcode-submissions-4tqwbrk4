class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i, j, m = 0, len(nums)-1, (len(nums)-1)//2

        while i <= j:
            
            if nums[m] > target:
                j = m - 1
                m = (i + j) // 2
                print(m, " = ", nums[m], " with ", i, j)

            elif nums[m] < target:
                i = m + 1
                m = (i + j) // 2
                print(m, " = ", nums[m], " with ", i, j)

            if nums[m] == target:
                return m

        return -1


