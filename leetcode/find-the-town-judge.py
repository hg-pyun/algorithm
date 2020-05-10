class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        checker = [0 for i in range(N + 1)]
        
        for [_, b] in trust:
            checker[b] += 1
            
        candidate = -1
    
        for i in range(N + 1):
            if checker[i] == (N - 1):
                candidate = i
        
        for [a, _] in trust:
            if a == candidate:
                return -1
        
        return candidate
