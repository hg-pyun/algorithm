class Solution:
    def convertToTitle(self, n: int) -> str:
        d = []
        while n > 0:
            n -= 1
            d.insert(0, chr(n%26 + 65))
            n //= 26
        
        return "".join(d)
