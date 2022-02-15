class Solution:
    def floodfill (self, grid, col, row, col_max, row_max, land):
        if col < 0 or row < 0:
            return
        elif col >= col_max or row >= row_max:
            return
        elif grid[col][row] != 1:
            return
        
        grid[col][row] = 0
        land.append([col, row])
        a = self.floodfill(grid, col + 1, row, col_max, row_max, land)
        b = self.floodfill(grid, col - 1, row, col_max, row_max, land)
        c = self.floodfill(grid, col, row + 1, col_max, row_max, land)
        d = self.floodfill(grid, col, row - 1, col_max, row_max, land)
        
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        len_col = len(grid1)
        len_row = len(grid1[0])
        
        count = 0
        
        for col in range(len_col):
            for row in range(len_row):
                if grid2[col][row] == 1:
                    land = []
                    overlay = True
                    self.floodfill(grid2, col, row, len_col, len_row, land)
                    for [i, j] in land:
                        if grid1[i][j] == 0:
                            overlay = False
                    if overlay:
                        count += 1
        return count
