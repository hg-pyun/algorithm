class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for v in range(start, start + 2 * n, 2):
            ans ^= v
        return ans
