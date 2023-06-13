class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        ans = ''
        start = False

        for i in range(len(num) - 1, -1, -1):
            if num[i] != "0":
                start = True
            
            if start:
                ans += num[i]
    
        return ''.join(reversed(ans))
