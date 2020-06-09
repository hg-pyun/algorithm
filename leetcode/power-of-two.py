class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        d = 2

        while d < (d << 30) and d <= n:
            if n / d == 1:
                return True
            d <<= 1
        
        return False
