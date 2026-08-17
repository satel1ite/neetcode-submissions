class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        if n == 1:
            return [['Q']]
        res = []
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [['.'] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c not in cols and (r-c) not in neg_diag and (r+c) not in pos_diag:
                    cols.add(c)
                    neg_diag.add(r-c)
                    pos_diag.add(r+c)
                    board[r][c] = 'Q'
                    backtrack(r+1)
                    cols.remove(c)
                    neg_diag.remove(r-c)
                    pos_diag.remove(r+c)
                    board[r][c] = '.'

        backtrack(0)
        return res
