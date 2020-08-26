class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        S = sorted(A)
        
        p = len(S) - 1
        largest = 0
        while p > 1:
            if S[p] < S[p-1] + S[p-2]:
                largest = max(largest, S[p] + S[p-1] + S[p-2])
            p = p - 1
                
        return largest
