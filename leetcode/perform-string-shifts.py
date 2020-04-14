class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        rs = 0
        for [d, a] in shift:
            if d > 0: rs += a
            else : rs -= a
    
        cut = rs > 0 and len(s) - abs(rs) or abs(rs)
        cut = cut % len(s)

        return s[cut:] + s[:cut]
        
