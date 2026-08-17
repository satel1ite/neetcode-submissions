class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word is None:
            return True
        if board == []:
            return False
        n = len(board)
        m = len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= n or c >= m or word[i] != board[r][c]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            board[r][c] = temp
            return res
        for r in range(n):
            for c in range(m):
                if dfs(r, c, 0):
                    return True
        return False