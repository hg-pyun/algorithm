class Solution:
    def minPartitions(self, n: str) -> int:
        ans = -1
        for i in n:
            ans = max(ans, int(i))
        
        return ans
