class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        ans = 0
        
        for i in range(0, len(timeSeries)):
            ans += duration
            
            if i == 0:
                continue
                
            current_time = timeSeries[i]
            before_time = timeSeries[i - 1]

            if before_time + duration > current_time:
                ans -= (before_time + duration - current_time)
                
        return ans
