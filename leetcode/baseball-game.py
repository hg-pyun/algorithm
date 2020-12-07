class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                v = stack.pop()
                stack.append(v)
                stack.append(v * 2)
            elif op == '+':
                if len(stack) > 1:                    
                    v1 = stack.pop()
                    v2 = stack.pop()
                    stack.append(v2)
                    stack.append(v1)
                    stack.append(v1 + v2)
            else:
                if op != 'C' and op != 'D' and op !='+':
                    stack.append(int(op))
                else:
                    stack.append(op)

        return sum(stack)
