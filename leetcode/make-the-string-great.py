class Solution:
    def makeGood(self, s: str) -> str:
        
        ans = s
        
        while True:    
            escape = True
            checker = [True for _ in range(len(ans))]
            
            for i in range(len(ans) - 1):
                if abs(ord(ans[i]) - ord(ans[i + 1])) == 32 and checker[i] is not False:
                    checker[i] = False
                    checker[i + 1] = False
                    escape = False
                    
            
            if escape:
                break

            new_string = ''
            for i in range(len(ans)):
                if checker[i]:
                    new_string += ans[i]

            ans = new_string
        
        return ans
