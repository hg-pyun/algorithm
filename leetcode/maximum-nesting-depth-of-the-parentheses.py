class Solution:
    def maxDepth(self, s: str) -> int:
        
        ans = 0
        dep = 0
        
        for char in s:
            if char == '(':
                dep += 1
            elif char == ')':
                ans = max(dep, ans)
                dep -= 1
        
        return ans
