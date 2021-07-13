class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        m, n = len(grid), len(grid[0])
        
        def flood_fill(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1;
                flood_fill(i, j+1) 
                flood_fill(i+1, j)
                flood_fill(i-1, j)
                flood_fill(i, j-1)
    
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    flood_fill(i, j)
    
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    flood_fill(i, j)
                    ans += 1
    
        return ans
