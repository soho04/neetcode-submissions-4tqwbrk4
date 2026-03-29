class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1

        while left <= right:

            mid = (left + right) // 2

            row, col = mid // n, mid % n

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
                



        # [1,   2,  4,  8] l 
        # [10, 11, 12, 13]
        # [14, 20, 30, 40] r

