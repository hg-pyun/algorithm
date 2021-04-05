class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        win_sum = 0 
        
        for i in range(0, k - 1):
            win_sum += arr[i]
        
        for i in range(len(arr) - k + 1):
            win_sum += arr[i + k - 1]
            
            if win_sum // k >= threshold:
                ans += 1
            
            win_sum -= arr[i]
            
        return ans
