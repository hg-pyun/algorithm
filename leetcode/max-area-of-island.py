class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        col_len = len(grid)
        row_len = len(grid[0])
        
        
        counter = 0
        def dfs(grid, i, j):
            if grid[i][j] == 0 or grid[i][j] == 2:
                return
            
            nonlocal counter
            counter += 1
            grid[i][j] = 2

            if j > 0:
                d1 = dfs(grid, i, j - 1)
            if j < row_len - 1:
                d2 = dfs(grid, i, j + 1)
            if i > 0:
                d3 = dfs(grid, i - 1, j)
            if i < col_len - 1:
                d4 = dfs(grid, i + 1, j)
        
        
        for i in range(col_len):
            for j in range(row_len):
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    ans = max(ans, counter)
                    counter = 0
        
        return ans
