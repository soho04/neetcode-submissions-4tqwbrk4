class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # total = len(matrix) * len(matrix[0])
    
        # i = matrix[0][0]
        # j = matrix[len(matrix)-1][len(matrix[0])-1]
        # m = matrix[i[0]+j[0]//2][i[1]+j[1]//2] 

        # while i <= j:

        array = []

        for list in matrix:
            array += list

        i = 0
        j = len(array)-1
        m = i + j // 2

        while i <= j:
            
            if array[m] > target:
                j = m - 1
                m = (i + j) // 2

            elif array[m] < target:
                i = m + 1
                m = (i + j) // 2

            if array[m] == target:
                return True

        return False


