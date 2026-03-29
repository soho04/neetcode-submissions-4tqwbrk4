class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n, m = len(matrix), len(matrix[0])

        left, right = 0, m*n-1

        while left <= right:

            middle = (left + right) // 2

            row = middle // m
            col = middle % m

            value = matrix[row][col]

            if value == target:
                return True

            if value > target:
                right = middle - 1
            
            else:
                left = middle + 1

        return False

        #  l  r
        # [1, 1]
