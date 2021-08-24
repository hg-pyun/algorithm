class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        need_count = 1
        while (n > 0):
            n -= need_count
            need_count += 1
        
        if n == 0:
            need_count -= 1
        else:
            need_count -= 2
            
        return need_count
