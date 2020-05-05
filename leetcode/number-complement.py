class Solution:
    def findComplement(self, num: int) -> int:
        mask = ~0
        while mask & num:
            mask <<= 1
        
        return ~mask & ~num
