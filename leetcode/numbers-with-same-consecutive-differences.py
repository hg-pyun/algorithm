class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        ans = []
        
        def dfs(num, addr ,dep):
            if dep == n - 1:
                ans.append(addr)
                return;
            
            positive = num + k
            negative = num - k
            
            positive <= 9 and dfs(positive, addr + str(positive), dep + 1)
            negative >= 0 and dfs(negative, addr + str(negative), dep + 1)
            
            
        for i in range(1, 10):
            dfs(i, str(i) , 0)
        
        return set(ans);
