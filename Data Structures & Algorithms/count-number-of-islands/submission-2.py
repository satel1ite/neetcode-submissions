class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def dfs(row, col):
            if grid[row][col] == '1':
                grid[row][col] = '0'
                if row + 1 < rows:
                    dfs(row + 1, col)
                if col + 1 < cols:
                    dfs(row, col + 1)
                if row - 1 >= 0:
                    dfs(row - 1, col)
                if col - 1 >= 0:
                    dfs(row, col - 1)
            return

                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count