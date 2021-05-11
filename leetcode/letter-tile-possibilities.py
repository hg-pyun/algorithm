class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        
        while n > 1:
            matches = n // 2
            team = matches
            remain = n % 2
            
            if remain:
                team += 1
            
            ans += matches
            n = team
            
        return ans
