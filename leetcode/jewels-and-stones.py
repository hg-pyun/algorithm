class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        checker = {}
        
        for j in J:
            checker[j] = True
        
        cnt = 0
        
        for s in S:
            if checker.get(s):
                cnt += 1
        
        return cnt
