class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        m5 = 0
        m10 = 0
        m20 = 0
        
        for bill in bills:
            if bill == 5:
                m5 += 1
            elif bill == 10:
                m10 += 1
                m5 -= 1
            elif bill == 20:
                if m10 > 0 and m5 > 0:
                    m5 -= 1
                    m10 -= 1
                else:
                    m5 -= 3
            
            if m5 < 0 or m10 < 0 or m20 <0:
                return False
        
        
        return True
