class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for c in range(9):
            r = 0
            col = [board[r][c] for r in range(9) if board[r][c] != '.']
            sett = set(col)
            if len(col) != len(set(col)):
                return False


        for r in range(9):
            lst = board[r]
            lst = [c for c in lst if c != '.']
            sett = set(lst)
            if len(lst) != len(sett):
                return False
            
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                square_list = []
                for i in range(3):
                    for j in range(3):
                        val = board[r+i][c+j]
                        if val != '.':
                            square_list.append(val)
                if len(square_list) != len(set(square_list)):
                    return False
        return True

