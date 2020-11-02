class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0 for i in range(num + 1)]

        for i in range(num + 1):
            t = i
            while t > 1:
                
                if t % 2 == 1:
                    ans[i] += 1 
                
                if t//2 < i:
                    ans[i] += ans[t//2]
                    break
                    
                t //= 2

            if t == 1:
                ans[i] += 1 
            
        return ans
