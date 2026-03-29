class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        square_map = defaultdict(list)

        for row in range(len(board)):
            
            for col in range(len(board[row])):
                
                if board[row][col] != ".":
                    
                    number = board[row][col]
                    square = ((row // 3), (col // 3))

                    if number in row_map[row] or number in col_map[col] or number in square_map[square]:
                        return False
                
                    row_map[row].append(number)
                    col_map[col].append(number)
                    square_map[square].append(number)

        print(col_map)

        return True

        

            # [[".",".","4",   ".",".",".",   "6","3","."],
            #  [".",".",".",   ".",".",".",   ".",".","."],
            #  ["5",".",".",   ".",".",".",   ".","9","."],

            #  [".",".",".",   "5","6",".",   ".",".","."],
            #  ["4",".","3",   ".",".",".",   ".",".","1"],
            #  [".",".",".",   "7",".",".",   ".",".","."],

            #  [".",".",".",   "5",".",".",   ".",".","."],
            #  [".",".",".",   ".",".",".",   ".",".","."],
            #  [".",".",".",   ".",".",".",   ".",".","."]]
        
                