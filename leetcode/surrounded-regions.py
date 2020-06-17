import queue;

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return []
        
        q = queue.Queue()
        
        r = len(board)
        c = len(board[0])
        
        for x in range(r):
            for y in range(c):
                letter = board[x][y]
                
                # check edge
                if (x == 0 or x == (r - 1)):
                    if letter == 'O':
                        q.put((x,y))
                        board[x][y] = 'V'
                
                if(y == 0 or y == (c - 1)):
                    if letter == 'O':
                        q.put((x,y))
                        board[x][y] = 'V'
        
        while q.qsize():
            (x, y) = q.get()
            if x < (r-1) and board[x+1][y] == 'O':
                q.put((x + 1, y))
                board[x + 1][y] = 'V'
            if x > 0 and board[x-1][y] == 'O':
                q.put((x - 1, y))
                board[x - 1][y] = 'V'
            if y < (c-1) and board[x][y+1] == 'O':
                q.put((x, y + 1))
                board[x][y + 1] = 'V'
            if y > 0 and board[x][y-1] == 'O':
                q.put((x, y - 1))
                board[x][y - 1] = 'V'
                
        for x in range(r):
            for y in range(c):
                letter = board[x][y]
                
                if letter == 'V':
                    board[x][y] = 'O'
                else:
                    board[x][y] = 'X'
