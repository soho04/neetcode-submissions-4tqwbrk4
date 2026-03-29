class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)

        for row in range(9):
            for col in range(9):

                if board[row][col] != ".":

                    number = board[row][col]
                    
                    square_x = col // 3
                    square_y = row // 3

                    print(square_map)

                    if number not in row_map[row] and number not in col_map[col] and number not in square_map[square_x, square_y]:
                        row_map[row].add(number)
                        col_map[col].add(number)
                        square_map[(square_x, square_y)].add(number)

                    else:
                        return False

        return True

        #[["1","2",".",    ".","3",".",     ".",".","."],
        # ["4",".",".",    "5",".",".",     ".",".","."],
        # [".","9","1",    ".",".",".",     ".",".","3"],

        # ["5",".",".",    ".","6",".",     ".",".","4"],
        # [".",".",".",    "8",".","3",     ".",".","5"],
        # ["7",".",".",    ".","2",".",     ".",".","6"],

        # [".",".",".",    ".",".",".",     "2",".","."],
        # [".",".",".",    "4","1","9",     ".",".","8"],
        # [".",".",".",    ".","8",".",     ".","7","9"]]

