class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        
        col_length = len(A)
        row_length = len(A[0])
        
        def dfs(land, col, row):
            if col < 0:
                return
            if col > col_length - 1:
                return
            if row < 0:
                return
            if row > row_length - 1:
                return
            
            if land[col][row] == 2 or land[col][row] == 0:
                return

            land[col][row] = 2
            
            dfs(land, col + 1, row)
            dfs(land, col - 1, row)
            dfs(land, col, row + 1)
            dfs(land, col, row - 1)
            
        
        for col in range(col_length):
            for row in range(row_length):
                if A[col][row] == 1:
                    if col == 0 or row == 0 or col == col_length - 1 or row == row_length - 1:
                        print('dfs', col, row)
                        dfs(A, col, row)
        
        
        ans = 0
        
        for col in range(col_length):
            for row in range(row_length):
                if A[col][row] == 1:
                    ans += 1

        return ans
