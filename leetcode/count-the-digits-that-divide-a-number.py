class Solution:
    def countDigits(self, num: int) -> int:

        count = 0

        for digit in str(num):
            if num % int(digit) == 0:
                count += 1
        
        return count
