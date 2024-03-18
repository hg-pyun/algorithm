class Solution:
    def pivotInteger(self, n: int) -> int:   

        if n == 1:
            return 1

        for i in range(n):
            left = 0
            right = 0
            for j in range(0, i + 1):
                left += j
            for k in range(i, n + 1):
                right += k
            
            if left == right:
                return i
    
        return -1
