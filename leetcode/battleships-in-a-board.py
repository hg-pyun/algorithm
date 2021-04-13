class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        col_len = len(board)
        row_len = len(board[0])
        
        def dfs(board, i, j):
            if board[i][j] == '.':
                return
                
            board[i][j] = '.'
            
            if j > 0:
                dfs(board, i, j - 1)
            if j < row_len - 1:
                dfs(board, i, j + 1)
            if i > 0:
                dfs(board, i - 1, j)
            if i < col_len - 1:
                dfs(board, i + 1, j)
                
        for i in range(col_len):
            for j in range(row_len):
                if board[i][j] == 'X':
                    ans += 1
                    dfs(board, i, j)
                    
        return ans
