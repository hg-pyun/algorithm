# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        ans = 0
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            
            j = guess(mid)
            
            if j == 0:
                return mid
            elif j > 0:
                l = mid  + 1
            else:
                r = mid - 1
