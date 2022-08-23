class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        ans = 0
        i = len(s) - 1  
        
        while (i >= 0):            
            if i == 0:
                ans += m[s[i]]
                break
            
            if s[i] == "V" and s[i - 1] == "I":
                ans += 4
                i -= 1
            elif s[i] == "X" and s[i - 1] == "I":
                ans += 9
                i -= 1
            elif s[i] == "L" and s[i - 1] == "X":
                ans += 40
                i -= 1
            elif s[i] == "C" and s[i - 1] == "X":
                ans += 90
                i -= 1
            elif s[i] == "D" and s[i - 1] == "C":
                ans += 400
                i -= 1
            elif s[i] == "M" and s[i - 1] == "C":
                ans += 900
                i -= 1
            else:
                ans += m[s[i]]
                
            i -= 1
        
        return ans
