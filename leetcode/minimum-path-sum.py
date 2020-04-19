class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        
        for y in range(n):
            for x in range(m):
                print(y, x, grid[y][x])
                if x is 0 and y is 0:
                    continue
                elif y is 0:
                    grid[y][x] += grid[y][x - 1]
                elif x is 0:
                    grid[y][x] += grid[y - 1][x]
                else:    
                    grid[y][x] += min(grid[y - 1][x], grid[y][x - 1])
        
        return grid[n - 1][m - 1]
