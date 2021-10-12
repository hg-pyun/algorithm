class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        
        ans = 0
        dep = 0
        for char in s:
            if char == '(':
                stack.append('(')
                dep += 1
            elif char == ')':
                stack.pop()
                ans = max(dep, ans)
                dep -= 1
        
        return ans
