class Solution:
    def toDigits(self, n, k):
        if n < k:
            return str(n)
        else:
            return self.toDigits(n // k, k) + str(n % k)

    def sumBase(self, n: int, k: int) -> int:
        result = self.toDigits(n, k)
        
        ans = 0
        for c in result:
            ans += int(c)

        return ans
