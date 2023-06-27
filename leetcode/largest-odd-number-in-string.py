class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        p = 0
        target = -1

        while p < len(num):
            if int(num[p]) % 2 == 1:
                target = p
            
            p += 1
        
        ans = num[0:target + 1]

        return ans
