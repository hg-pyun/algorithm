class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = 2**31 - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if x < mid * mid:
                hi = mid
            else:
                lo = mid + 1

        return lo - 1
