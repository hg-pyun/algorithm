class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        ans = []
        diff = []
        
        for i in range(n):
            if i+1 in target:
                ans.append('Push')
                diff.append(i+1)
            else:
                ans.append('Push')
                ans.append('Pop')
                
            if len(diff) == len(target):
                return ans
