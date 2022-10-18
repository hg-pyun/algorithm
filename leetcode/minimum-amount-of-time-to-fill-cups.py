class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        second = 0
        
        while (amount[0] != 0 or amount[1] != 0 or amount[2] != 0):
            
            amount.sort(reverse=True)
            second += 1
            
            fill = 0
            
            if amount[0] != 0:
                amount[0] -= 1
                fill += 1
            
            if amount[1] != 0:
                amount[1] -= 1
                fill += 1
            
            if fill == 2:
                continue
            
            if amount[2] != 0:
                amount[2] -= 1
                
                
        return second
