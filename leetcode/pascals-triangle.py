class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for i in range(numRows):
            if i == 0:
                ans.append([1])
                continue
            elif i == 1:
                ans.append([1,1])
                continue
            
            # fill center
            inner = [1]
            before = ans[i-1]
            
            for j in range(i):
                if j != i - 1:
                    inner.append(before[j] + before[j+1])
            
            inner.append(1)
            ans.append(inner)
            
        return ans
