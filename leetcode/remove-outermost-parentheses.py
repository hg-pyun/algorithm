class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        is_assemble = False
        assembler = ""
        result = ""
        for p in S:
            if p == "(":
                if is_assemble:
                    assembler += p
                if not stack:
                    is_assemble = True
                stack.append(p)
            else:
                stack.pop()
                if not stack:
                    result += assembler
                    assembler = ""
                    is_assemble = False
                if is_assemble:
                    assembler += p
        return result
    
