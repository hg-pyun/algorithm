class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            
            if not stack:
                return False 
            
            if char == ')':
                pop_char = stack.pop();
                if pop_char != '(':
                    return False
                
            if char == ']':
                pop_char = stack.pop();
                if pop_char != '[':
                    return False
            
            if char == '}':
                pop_char = stack.pop();
                if pop_char != '{':
                    return False
                
        return not stack
      
