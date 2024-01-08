class Solution:
    def arrangeCoins(self, n: int) -> int:

        stair = 0
        i = 1

        while n > 0:
            n -= i
            i += 1
            stair += 1

        if n == 0:
            return stair
        else:
            return stair - 1
