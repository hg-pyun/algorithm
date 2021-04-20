class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        lc = 0
        rc = 0
        for c in s:
            if c == 'R':
                lc += 1
            else:
                rc += 1
            if lc == rc:
                lc = 0
                rc = 0
                ans += 1
        return ans
