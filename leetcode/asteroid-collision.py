class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for a in asteroids:
            if len(stack) == 0:
                stack.append(a)
                continue
            
            top = stack.pop()
            
            while True:
                if (top > 0 and a > 0) or top < 0:
                    stack.append(top)
                    stack.append(a)
                    break;
                elif abs(top) == abs(a):
                    break;
                else:
                    if abs(top) < abs(a):
                        if len(stack) != 0:
                            top = stack.pop()
                        else:
                            stack.append(a)
                            break;
                    else:
                        stack.append(top)
                        break;
        
        return stack
