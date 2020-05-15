class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
    
        max_current_sum = 0
        max_sum = -math.inf
        min_current_sum = 0
        min_sum = math.inf
        for i in range(len(A)):
            max_current_sum = max(A[i], max_current_sum + A[i])
            max_sum = max(max_current_sum, max_sum)
            min_current_sum = min(A[i], min_current_sum + A[i])
            min_sum = min(min_current_sum, min_sum)
                
        return max_sum > 0 and max(max_sum, sum(A) - min_sum) or max_sum
