class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        
        count = 0
        for y in range(1, n + 1):
            for x in range(1, m + 1):
                if matrix[y - 1][x - 1] == 1:
                    dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1]) + 1
                    count += dp[y][x]
                    
        return count
