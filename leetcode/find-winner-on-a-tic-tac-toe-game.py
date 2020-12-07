class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        def check_vertical(board, char):
            for x in range(3):
                if board[y][0] == char and board[y][1] == char and board[y][2] == char:
                    return True
            return False
        
        def check_horizontal(board, char):
            for x in range(3):
                if board[0][x] == char and board[1][x] == char and board[2][x] == char:
                    return True
            return False
        
        def check_cross(board, char):
            if board[0][0] == char and board[1][1] == char and board[2][2] == char:
                return True
            elif board[2][0] == char and board[1][1] == char and board[0][2] == char:
                return True
            return False
                
        
        def check_result(board):
            if check_vertical(board, 'X') or check_horizontal(board, 'X') or check_cross(board, 'X'):
                return 'A'
            elif check_vertical(board, 'O') or check_horizontal(board, 'O') or check_cross(board, 'O'):
                return 'B'
        
        for i in range(len(moves)):
            [x, y] = moves[i]
            if i % 2 == 0:
                board[y][x] = 'X'
            else:
                board[y][x] = 'O'
        
        result = check_result(board)
        if result is None and len(moves) == 9:
            return 'Draw'
        
        return 'Pending' if result is None else result
